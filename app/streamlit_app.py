"""
HabitSync — Dashboard Experimental (Streamlit)
================================================

Identidade visual "Dark Luminescent / Neon" (exclusiva deste app —
não é a mesma paleta usada no HTML de apresentação de quarta-feira,
que agora foi unificada sob pedido; ver nota no chat sobre a mudança).

Este dashboard consome o MESMO motor de recomendação validado no notebook
(`src/habitsync/engine.py`), sem reimplementar nenhuma regra de negócio.

Como rodar (Mac, a partir da raiz do repositório):
    python3 -m pip install -r requirements.txt
    python3 -m streamlit run app/streamlit_app.py
"""

import os
import sys

import pandas as pd
import streamlit as st

# Garante que "src/" esteja no path, independentemente de onde o Streamlit for iniciado
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "src"))

from habitsync import engine  # noqa: E402

# ---------------------------------------------------------------------------
# Configuração de página
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="HabitSync · Dashboard Experimental",
    page_icon="🪞",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# CSS: identidade "Dark Luminescent / Neon" + fundo de pétalas contemplativo
# ---------------------------------------------------------------------------

NEON_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@200;300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root{
  --bg:#060B14; --surface:#0B1424; --surface2:#101B30;
  --magenta:#FF00BA; --magenta-dim:#8A0090; --magenta-glow:rgba(255,0,186,.18);
  --cyan:#00A7FF; --cyan-dim:#0080B8; --cyan-glow:rgba(0,167,255,.18);
  --text:#F2ECFA; --text70:rgba(242,236,250,.7); --text50:rgba(242,236,250,.5);
  --border:rgba(0,167,255,.32); --border-hover:rgba(255,0,186,.6);
  --font:'Inter',system-ui,sans-serif; --mono:'JetBrains Mono',monospace;
}

/* Fundo geral do app */
.stApp{
  background: radial-gradient(ellipse 80% 55% at 50% -8%, var(--magenta-glow) 0%, transparent 62%), var(--bg) !important;
  color: var(--text);
  font-family: var(--font);
}
section[data-testid="stSidebar"]{
  background: var(--surface) !important;
  border-right: 1px solid var(--border);
}
h1, h2, h3, h4, p, span, label, li { color: var(--text) !important; font-family: var(--font); }
.stApp, .stMarkdown, .stText { color: var(--text); }

/* Botão principal */
.stButton>button{
  background: linear-gradient(135deg, var(--magenta), var(--magenta-dim));
  color: #fff; border: none; border-radius: 12px; padding: 10px 22px;
  font-weight: 600; letter-spacing: .02em; transition: box-shadow .25s, transform .25s;
}
.stButton>button:hover{ box-shadow: 0 0 24px var(--magenta-glow), 0 0 12px var(--cyan-glow); transform: translateY(-1px); }

/* Selectbox e widgets: fundo vidro */
div[data-baseweb="select"]>div{
  background: rgba(255,255,255,.05) !important; border: 1px solid var(--border) !important; border-radius: 10px !important;
}

/* Cartão de vidro (glassmorphism) reutilizável */
.glass-card{
  background: linear-gradient(rgba(255,255,255,.05), rgba(255,255,255,.05)), var(--surface);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  border: 1px solid var(--border); border-radius: 16px;
  padding: 20px 22px; margin-bottom: 14px;
  transition: border-color .3s, box-shadow .3s;
}
.glass-card:hover{ border-color: var(--border-hover); box-shadow: 0 16px 40px var(--magenta-glow), 0 0 24px var(--cyan-glow); }

.badge{
  display:inline-flex; align-items:center; gap:5px; background:rgba(255,0,186,.12);
  border:1px solid var(--border); border-radius:999px; padding:4px 12px;
  font-family:var(--mono); font-size:.68rem; color:var(--magenta) !important; margin-right:6px;
}
.badge-cyan{ background:rgba(0,167,255,.12); border-color:var(--border); color:var(--cyan) !important; }

.score-bar-track{ background: rgba(255,255,255,.08); border-radius:999px; height:8px; overflow:hidden; margin-top:4px; }
.score-bar-fill{ height:100%; background: linear-gradient(90deg, var(--magenta), var(--cyan)); border-radius:999px; }

.banner-synthetic{
  background: rgba(0,167,255,.06); border:1px solid var(--border); border-radius:12px;
  padding:12px 16px; font-size:.82rem; color:var(--text70) !important; margin-bottom:18px;
}

/* --------------------------------------------------------------------- */
/* Fundo de pétalas: lento, orgânico, deriva lateral tipo pêndulo,       */
/* rotação não-uniforme, baixa densidade (contemplativo, não confete)    */
/* --------------------------------------------------------------------- */
#petals-bg{ position:fixed; inset:0; pointer-events:none; z-index:0; overflow:hidden; }
.petal{
  position:absolute; top:-5%; width:var(--size); height:var(--size);
  left:var(--left); border-radius:50% 0 50% 50%;
  background: linear-gradient(135deg, var(--magenta), var(--cyan)); opacity:.35;
  animation: petal-fall var(--duration) linear var(--delay) infinite, petal-sway calc(var(--duration) * .4) ease-in-out var(--delay) infinite alternate;
}
@keyframes petal-fall{ from{ transform: translateY(-10vh) rotateZ(0deg);} to{ transform: translateY(110vh) rotateZ(var(--spin));} }
@keyframes petal-sway{ from{ margin-left:-24px;} to{ margin-left:24px;} }
@media (prefers-reduced-motion: reduce){ .petal{ animation:none; opacity:.12; } }
</style>
"""

PETALS_HTML = """
<div id="petals-bg">
""" + "\n".join(
    f'<div class="petal" style="--size:{size}px; --left:{left}%; --duration:{duration}s; --delay:{delay}s; --spin:{spin}deg;"></div>'
    for size, left, duration, delay, spin in [
        (14, 6, 22, 0, 300), (10, 18, 19, 3, -220), (16, 30, 25, 1.5, 260),
        (11, 45, 21, 5, -300), (13, 58, 24, 2, 240), (9, 70, 18, 4.5, -260),
        (15, 82, 23, 1, 320), (12, 92, 20, 6, -240),
    ]
) + "\n</div>"

st.markdown(NEON_CSS, unsafe_allow_html=True)
st.markdown(PETALS_HTML, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Carregamento de dados (cacheado)
# ---------------------------------------------------------------------------

@st.cache_data
def _load():
    products_df, users_df, interactions_df = engine.load_data()
    interaction_matrix = engine.build_interaction_matrix(interactions_df, products_df)
    return products_df, users_df, interactions_df, interaction_matrix


products_df, users_df, interactions_df, interaction_matrix = _load()
couple_ids = sorted(users_df["couple_id"].unique().tolist())

# Nomes miticos por casal — vindos do notebook atualizado (Fabi, 02/09).
# Nota: apenas Adao/Eva, Eros/Psique, Rama/Sita e Shiva/Shakti tem pilar
# tecnico documentado ate agora (ver README). Os demais sao apenas labels
# de exibicao amigaveis por enquanto — nao forcar pilar tecnico sem curadoria.
COUPLE_MYTH_NAMES = {
    "C001": "Eros e Psiquê", "C002": "Adão e Eva", "C003": "Rama e Sita",
    "C004": "Zeus e Hera", "C005": "Hades e Perséfone", "C006": "Ulisses e Penélope",
    "C007": "Orfeu e Eurídice", "C008": "Teseu e Ariadne", "C009": "Píramo e Tisbe",
    "C010": "Ísis e Osíris", "DEMO_COMPAT": "Romeu e Julieta", "DEMO_CONFLICT": "Bonnie e Clyde",
}


def _couple_label(cid: str) -> str:
    myth = COUPLE_MYTH_NAMES.get(cid)
    return f"{myth} · {cid}" if myth else cid

# ---------------------------------------------------------------------------
# Cabeçalho
# ---------------------------------------------------------------------------

st.markdown(
    """
    <div style="margin-bottom:6px;">
      <span style="font-family:var(--mono); font-size:.7rem; letter-spacing:.12em; color:var(--cyan);">
        MINDFUL AI · HABITSYNC
      </span>
    </div>
    <h1 style="font-size:2.1rem; font-weight:700; margin-bottom:4px;">HabitSync — Dashboard Experimental</h1>
    <p style="color:var(--text70); max-width:640px; margin-bottom:18px;">
      Duas linhas diferentes, um mesmo espaço harmônico. Recomendações de treino e alimentação
      para casais, com <b>prioridade absoluta</b> a alergias e restrições — e explicabilidade
      bilíngue em cada sugestão.
    </p>
    <div class="banner-synthetic">
      ⚠️ Aviso: todos os dados usados são <b>sintéticos</b> (fins educacionais). As recomendações são
      informativas e não substituem orientação nutricional, médica ou de treinamento profissional.
    </div>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar: seleção do casal
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("### 👥 Selecionar casal")
    couple_id = st.selectbox(
        "ID do casal", couple_ids,
        index=couple_ids.index("DEMO_CONFLICT") if "DEMO_CONFLICT" in couple_ids else 0,
        format_func=_couple_label,
    )

    couple_users = users_df[users_df["couple_id"] == couple_id]
    if len(couple_users) == 2:
        user_a, user_b = couple_users.iloc[0], couple_users.iloc[1]
        for label, u in [("Partner A", user_a), ("Partner B", user_b)]:
            st.markdown(
                f"""
                <div class="glass-card" style="padding:14px 16px;">
                  <div style="font-family:var(--mono); font-size:.65rem; color:var(--cyan);">{label}</div>
                  <div style="font-size:.85rem; margin-top:4px;">
                    🎯 {u['goals']}<br>
                    🍽️ {u['dietary_restrictions']}<br>
                    🏋️ {u['training_type']}
                  </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    run = st.button("✨ Gerar recomendação", use_container_width=True)

# ---------------------------------------------------------------------------
# Corpo principal: resultado da recomendação
# ---------------------------------------------------------------------------

if run:
    result = engine.recommend_for_couple(couple_id, products_df, users_df, interaction_matrix, top_k=3)

    excluded = result.n_candidates_before_safety - result.n_candidates_after_safety
    st.markdown(
        f"""
        <div class="glass-card">
          <span class="badge">🛡️ Filtro de segurança</span>
          <span style="color:var(--text70);">
            {result.n_candidates_after_safety} de {result.n_candidates_before_safety} produtos passaram
            {f" — <b style='color:var(--magenta)'>{excluded} excluído(s)</b> por alergia/restrição de um dos parceiros" if excluded else " (nenhuma restrição eliminou produtos deste casal)"}
          </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if result.top.empty:
        st.warning("Nenhum produto seguro disponível para este casal com os critérios atuais.")
    else:
        cols = st.columns(len(result.top))
        for col, (_, row) in zip(cols, result.top.iterrows()):
            with col:
                pct = int(row["final_score"] * 100)
                st.markdown(
                    f"""
                    <div class="glass-card">
                      <div style="font-size:.66rem; font-family:var(--mono); color:var(--text50);">{row['product_id']} · {row['brand']}</div>
                      <div style="font-weight:600; margin:4px 0 8px;">{row['description']}</div>
                      <span class="badge">R$ {row['price']:.2f}</span>
                      <span class="badge badge-cyan">{row['category']}</span>
                      <div style="margin-top:12px; font-size:.68rem; color:var(--text50);">SCORE FINAL · {pct}%</div>
                      <div class="score-bar-track"><div class="score-bar-fill" style="width:{pct}%;"></div></div>
                      <div style="margin-top:12px; font-size:.66rem; color:var(--text50); display:flex; justify-content:space-between;">
                        <span>conteúdo {row['content_score']:.2f}</span><span>colaborativo {row['collaborative_score']:.2f}</span>
                      </div>
                      <p style="font-size:.8rem; color:var(--text70); margin-top:12px; line-height:1.5;">
                        🇧🇷 {row['explanation_pt']}
                      </p>
                      <p style="font-size:.78rem; color:var(--text50); margin-top:6px; line-height:1.5; font-style:italic;">
                        🇬🇧 {row['explanation_en']}
                      </p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
else:
    st.info("Selecione um casal na barra lateral e clique em **Gerar recomendação** para ver o motor em ação.")

st.markdown(
    """
    <div style="margin-top:32px; padding-top:16px; border-top:1px solid rgba(255,255,255,.08); font-size:.72rem; color:var(--text50);">
      PUC-SP · FACEI · Artificial Intelligence Knowledge Systems &amp; Intelligent Agents · Profa. Sandra Bozolan<br>
      Autora: Fabiana Campanari · ॐ Mindful AI · github.com/Mindful-AI-Research
    </div>
    """,
    unsafe_allow_html=True,
)
