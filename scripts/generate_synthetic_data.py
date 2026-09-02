"""
Gerador de dataset sintético para o NewVoiceHabits.

Este script cria 3 tabelas 100% sintéticas (nenhum dado real de usuário ou
produto), usadas para demonstrar o pipeline de recomendação híbrido descrito
no briefing "Assistente Inteligente de Recomendação":

    products.csv     -> catálogo de produtos de treino/dieta
    users.csv        -> perfis dos casais (dois parceiros por couple_id)
    interactions.csv -> histórico simulado de compras/avaliações/visualizações,
                         usado como base da "filtragem colaborativa (simulação)"

Todas as tabelas incluem a coluna is_synthetic = True, reforçando no próprio
dado que nenhuma informação real foi utilizada (requisito de Responsible AI
definido na Fase 2).
"""

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

# ---------------------------------------------------------------------------
# 1. PRODUCTS
# ---------------------------------------------------------------------------

CATEGORIES = {
    "protein": ["whey", "isolate", "hydrolyzed", "vegan_protein"],
    "creatine": ["creatine_monohydrate", "creatine_hcl"],
    "vitamins": ["multivitamin", "vitamin_d", "omega_3"],
    "healthy_food": ["snack_bar", "granola", "oatmeal"],
    "equipment": ["resistance_bands", "yoga_mat", "dumbbell_set"],
}

BRANDS = ["VitaFit", "PureNutri", "GreenGain", "IronCore", "BalancePlus"]

TAGS_POOL = [
    "#vegan", "#gluten_free", "#lactose_free", "#high_protein",
    "#low_sugar", "#organic", "#no_added_sugar",
]

def make_products(n=25):
    rows = []
    for i in range(1, n + 1):
        category = random.choice(list(CATEGORIES.keys()))
        subcategory = random.choice(CATEGORIES[category])
        is_vegan = subcategory == "vegan_protein" or random.random() < 0.3
        tags = set()
        if is_vegan:
            tags.add("#vegan")
        tags.update(random.sample(TAGS_POOL, k=random.randint(1, 3)))

        rows.append({
            "product_id": f"P{i:03d}",
            "category": category,
            "subcategory": subcategory,
            "brand": random.choice(BRANDS),
            "price": round(random.uniform(19.9, 249.9), 2),
            "ingredients": f"ingredient profile for {subcategory}",
            "description": f"{subcategory.replace('_', ' ').title()} product for {category.replace('_', ' ')} goals",
            "tags": ",".join(sorted(tags)),
            "is_synthetic": True,
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# 2. USERS (couples)
# ---------------------------------------------------------------------------

GOALS = ["muscle_gain", "weight_loss", "endurance"]
RESTRICTIONS = ["vegan", "vegetarian", "lactose_free", "none"]
TRAINING_TYPES = ["bodybuilding", "crossfit", "yoga"]

def make_users(n_couples=10):
    rows = []
    for c in range(1, n_couples + 1):
        couple_id = f"C{c:03d}"
        for role in ["partner_a", "partner_b"]:
            rows.append({
                "user_id": f"{couple_id}_{role}",
                "couple_id": couple_id,
                "role": role,
                "goals": random.choice(GOALS),
                "dietary_restrictions": random.choice(RESTRICTIONS),
                "training_type": random.choice(TRAINING_TYPES),
                "is_synthetic": True,
            })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# 3. INTERACTIONS (simulated collaborative-filtering signal)
# ---------------------------------------------------------------------------

EVENT_TYPES = ["view", "rating", "purchase"]

def make_interactions(users_df, products_df, per_user_min=5, per_user_max=10):
    rows = []
    interaction_id = 1
    base_date = datetime(2026, 1, 1)

    # Vieses de compatibilidade produto <-> perfil, para que o histórico
    # simulado seja coerente com o objetivo/restrição de cada usuário
    # (essencial para uma demonstração defensável da filtragem colaborativa).
    def compatible(product, user):
        score = 0
        if user["dietary_restrictions"] == "vegan" and "#vegan" in product["tags"]:
            score += 2
        if user["goals"] == "muscle_gain" and product["category"] in ("protein", "creatine"):
            score += 2
        if user["goals"] == "weight_loss" and product["category"] in ("healthy_food", "vitamins"):
            score += 1
        if user["training_type"] == "yoga" and product["category"] == "equipment":
            score += 1
        return score + 1  # peso mínimo para permitir alguma exploração aleatória

    for _, user in users_df.iterrows():
        weights = products_df.apply(lambda p: compatible(p, user), axis=1).values
        weights = weights / weights.sum()
        n_events = random.randint(per_user_min, per_user_max)
        chosen = np.random.choice(products_df["product_id"], size=n_events, p=weights, replace=True)

        for product_id in chosen:
            event_type = random.choices(EVENT_TYPES, weights=[0.5, 0.3, 0.2])[0]
            value = (
                round(random.uniform(3.0, 5.0), 1) if event_type == "rating"
                else 1
            )
            rows.append({
                "interaction_id": f"I{interaction_id:04d}",
                "user_id": user["user_id"],
                "product_id": product_id,
                "event_type": event_type,
                "value": value,
                "timestamp": (base_date + timedelta(days=random.randint(0, 120))).isoformat(),
                "is_synthetic": True,
            })
            interaction_id += 1

    return pd.DataFrame(rows)


if __name__ == "__main__":
    products_df = make_products(n=25)
    users_df = make_users(n_couples=10)
    interactions_df = make_interactions(users_df, products_df)

    out_dir = "/mnt/user-data/outputs/data/synthetic"
    products_df.to_csv(f"{out_dir}/products.csv", index=False)
    users_df.to_csv(f"{out_dir}/users.csv", index=False)
    interactions_df.to_csv(f"{out_dir}/interactions.csv", index=False)

    print("products:", products_df.shape)
    print("users:", users_df.shape)
    print("interactions:", interactions_df.shape)
    print("\nAmostra de products:\n", products_df.head(3).to_string())
    print("\nAmostra de users:\n", users_df.head(4).to_string())
    print("\nAmostra de interactions:\n", interactions_df.head(4).to_string())
