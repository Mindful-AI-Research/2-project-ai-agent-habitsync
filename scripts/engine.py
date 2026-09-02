"""
HabitSync — Recommendation Engine
==================================

Porte fiel, 1:1, da lógica validada em `notebooks/habitsync_mvp.ipynb`
(37 células, todos os asserts passando, 4 cenários de demonstração).

Nenhuma regra de negócio foi alterada nesta portabilidade: apenas o
código foi reorganizado em funções importáveis, para ser reutilizado
tanto pelo notebook quanto pelo dashboard Streamlit (`app/streamlit_app.py`).

Princípio inegociável (não mexer): o filtro de segurança (alergias e
restrições alimentares) roda ANTES de qualquer pontuação/ranking, nunca depois.
"""

from __future__ import annotations

import os
from dataclasses import dataclass

import numpy as np
import pandas as pd

# --------------------------------------------------------------------------
# 1. Carregamento de dados
# --------------------------------------------------------------------------

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "synthetic")


def load_data(data_dir: str = DATA_DIR) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Carrega os 3 datasets sintéticos (produtos, usuários, interações)."""
    products_df = pd.read_csv(os.path.join(data_dir, "products.csv"))
    users_df = pd.read_csv(os.path.join(data_dir, "users.csv"))
    interactions_df = pd.read_csv(os.path.join(data_dir, "interactions.csv"))
    return products_df, users_df, interactions_df


# --------------------------------------------------------------------------
# 2. Prioridade absoluta: restrições alimentares e alérgenos (filtro de segurança)
# --------------------------------------------------------------------------

RESTRICTION_RULE = {
    "vegan": lambda p: "#vegan" in str(p["tags"]),
    "vegetarian": lambda p: "#vegetarian" in str(p["tags"]),
    "lactose_free": lambda p: "lactose" not in str(p["allergens"]),
    "gluten_free": lambda p: "gluten" not in str(p["allergens"]),
    "nut_allergy": lambda p: "nuts" not in str(p["allergens"]),
    "none": lambda p: True,
}


def is_safe_for_user(product: pd.Series, user: pd.Series) -> bool:
    rule = RESTRICTION_RULE.get(user["dietary_restrictions"], lambda p: True)
    return bool(rule(product))


def is_safe_for_couple(product: pd.Series, user_a: pd.Series, user_b: pd.Series) -> bool:
    return is_safe_for_user(product, user_a) and is_safe_for_user(product, user_b)


# --------------------------------------------------------------------------
# 3. Filtragem baseada em conteúdo
# --------------------------------------------------------------------------

GOAL_CATEGORY = {
    "muscle_gain": ["protein", "creatine"],
    "weight_loss": ["healthy_food", "vitamins"],
    "endurance": ["vitamins", "healthy_food"],
}
TRAINING_CATEGORY_BONUS = {
    "yoga": ["equipment"],
    "crossfit": ["equipment", "protein"],
    "bodybuilding": ["protein", "creatine"],
}


def content_score_for_user(product: pd.Series, user: pd.Series) -> float:
    score = 0.0
    if product["category"] in GOAL_CATEGORY.get(user["goals"], []):
        score += 2.0
    if product["category"] in TRAINING_CATEGORY_BONUS.get(user["training_type"], []):
        score += 1.0
    return score


def content_scores_for_couple(candidates_df: pd.DataFrame, user_a: pd.Series, user_b: pd.Series) -> pd.Series:
    score_a = candidates_df.apply(lambda p: content_score_for_user(p, user_a), axis=1)
    score_b = candidates_df.apply(lambda p: content_score_for_user(p, user_b), axis=1)
    return (score_a + score_b) / 2.0


# --------------------------------------------------------------------------
# 4. Filtragem colaborativa (simulada, fins educacionais)
# --------------------------------------------------------------------------

def build_interaction_matrix(interactions_df: pd.DataFrame, products_df: pd.DataFrame) -> pd.DataFrame:
    matrix = pd.pivot_table(
        interactions_df, index="user_id", columns="product_id",
        values="value", aggfunc="sum", fill_value=0.0,
    )
    matrix = matrix.reindex(columns=products_df["product_id"], fill_value=0.0)
    return matrix


def simulate_collaborative_filter(user_id: str, interaction_matrix: pd.DataFrame) -> pd.Series:
    if user_id not in interaction_matrix.index:
        return pd.Series(0.0, index=interaction_matrix.columns)
    target = interaction_matrix.loc[user_id].values
    others = interaction_matrix.drop(index=user_id)
    if others.empty:
        return pd.Series(0.0, index=interaction_matrix.columns)
    target_norm = np.linalg.norm(target)
    sims = []
    for _, row in others.iterrows():
        v = row.values
        denom = target_norm * np.linalg.norm(v)
        sims.append(float(np.dot(target, v) / denom) if denom > 0 else 0.0)
    sims = np.array(sims)
    if sims.sum() <= 0:
        return pd.Series(0.0, index=interaction_matrix.columns)
    weighted = others.T.values @ sims
    weighted = weighted / (sims.sum() + 1e-9)
    return pd.Series(weighted, index=interaction_matrix.columns)


def collaborative_scores_for_couple(user_a_id, user_b_id, interaction_matrix, candidate_ids) -> pd.Series:
    collab_a = simulate_collaborative_filter(user_a_id, interaction_matrix)
    collab_b = simulate_collaborative_filter(user_b_id, interaction_matrix)
    combined = (collab_a + collab_b) / 2.0
    return combined.reindex(candidate_ids).fillna(0.0)


# --------------------------------------------------------------------------
# 5. Ranking híbrido ponderado
# --------------------------------------------------------------------------

def _normalize(series: pd.Series) -> pd.Series:
    lo, hi = series.min(), series.max()
    if hi - lo < 1e-9:
        return pd.Series(0.5, index=series.index)
    return (series - lo) / (hi - lo)


def weighted_rank(candidates_df, content_scores, collaborative_scores,
                   weight_content: float = 0.6, weight_collaborative: float = 0.4) -> pd.DataFrame:
    result = candidates_df.copy().reset_index(drop=True)
    content_scores = content_scores.reset_index(drop=True)
    collaborative_scores = collaborative_scores.reset_index(drop=True)

    result["content_score"] = content_scores.round(3)
    result["collaborative_score"] = collaborative_scores.round(3)
    final = (weight_content * _normalize(content_scores)
             + weight_collaborative * _normalize(collaborative_scores))
    result["final_score"] = final.round(3)
    return result.sort_values("final_score", ascending=False).reset_index(drop=True)


# --------------------------------------------------------------------------
# 6. Explicabilidade estruturada e bilíngue
# --------------------------------------------------------------------------

def explain_recommendation(product_row: pd.Series, user_a: pd.Series, user_b: pd.Series) -> dict:
    reasons_pt, reasons_en = [], []

    if (product_row["category"] in GOAL_CATEGORY.get(user_a["goals"], [])
            or product_row["category"] in GOAL_CATEGORY.get(user_b["goals"], [])):
        reasons_pt.append("alinhado aos objetivos do casal")
        reasons_en.append("matches the couple's goals")

    if user_a["dietary_restrictions"] != "none" or user_b["dietary_restrictions"] != "none":
        reasons_pt.append("respeita as restrições alimentares informadas por ambos")
        reasons_en.append("respects both partners' dietary restrictions")

    if not reasons_pt:
        reasons_pt.append("boa avaliação entre casais com perfil semelhante (simulado)")
        reasons_en.append("well rated among couples with a similar profile (simulated)")

    return {
        "reasons_pt": reasons_pt,
        "reasons_en": reasons_en,
        "text_pt": f"Recomendamos {product_row['description']} porque {', '.join(reasons_pt)}.",
        "text_en": f"We recommend {product_row['description']} because it is {', '.join(reasons_en)}.",
    }


# --------------------------------------------------------------------------
# 7. Orquestração: recomendação para um casal
# --------------------------------------------------------------------------

@dataclass
class RecommendationResult:
    top: pd.DataFrame
    user_a: pd.Series
    user_b: pd.Series
    n_candidates_before_safety: int
    n_candidates_after_safety: int


def recommend_for_couple(couple_id: str, products_df: pd.DataFrame, users_df: pd.DataFrame,
                          interaction_matrix: pd.DataFrame, top_k: int = 3) -> RecommendationResult:
    couple_users = users_df[users_df["couple_id"] == couple_id]
    assert len(couple_users) == 2, f"couple_id {couple_id} não possui exatamente 2 usuários"
    user_a, user_b = couple_users.iloc[0], couple_users.iloc[1]

    # PRIORIDADE ABSOLUTA: filtro de segurança antes de qualquer ranking
    safe_mask = products_df.apply(lambda p: is_safe_for_couple(p, user_a, user_b), axis=1)
    candidates_df = products_df[safe_mask & products_df["availability"]].reset_index(drop=True)

    content_scores = content_scores_for_couple(candidates_df, user_a, user_b)
    collaborative_scores = collaborative_scores_for_couple(
        user_a["user_id"], user_b["user_id"], interaction_matrix, candidates_df["product_id"]
    )
    ranked = weighted_rank(candidates_df, content_scores, collaborative_scores)
    top = ranked.head(top_k).copy()

    explanations = [explain_recommendation(row, user_a, user_b) for _, row in top.iterrows()]
    top["explanation_pt"] = [e["text_pt"] for e in explanations]
    top["explanation_en"] = [e["text_en"] for e in explanations]

    return RecommendationResult(
        top=top,
        user_a=user_a,
        user_b=user_b,
        n_candidates_before_safety=len(products_df),
        n_candidates_after_safety=len(candidates_df),
    )
