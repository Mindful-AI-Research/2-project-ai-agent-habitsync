# 🎼 HabitSync — AI Recommendation Agent EXPLORATORY
###  **An AI agent that gives couples voice-guided, explainable recommendations for training and diet products.**

<br><br>

> 🚧 **Academic MVP — validated.** Full production-grade documentation, backend, and web app are part of an active, phased roadmap.

<br><br>


<!-- ========= START APP BADGE ========= -->
<p align="center" style="margin: 0;">
  <a href="https://effulgent-banoffee-ed032c.netlify.app/" rel="noopener noreferrer">
    <img 
      src="https://img.shields.io/badge/Live%20App-HabitSync-0f172a?style=for-the-badge&logo=netlify&logoColor=white" 
      alt="Live App HabitSync"
      style="height: 38px; width: auto;"
    />
  </a>
</p>
<!-- ========= END APP BADGE ========= -->



<br><br>

## 📚 Table of Contents

- [🎯 What is HabitSync?](#-what-is-habitsync)
- [🎼 Music, Meaning & Human-Centered AI](#-music-meaning--human-centered-ai)
  - [🎼 The Musical Identity](#-the-musical-identity)
  - [🧠 Human-Centered AI](#-human-centered-ai)
  - [✨ The Core Message](#-the-core-message)
- [🔍 How the Recommendation Engine Works](#-how-the-recommendation-engine-works)
- [🏗️ Phase 2 — Complete Architecture: NewVoiceHabits](#️-phase-2--complete-architecture-newvoicehabits)
  - [System Architecture](#system-architecture)
  - [Core Recommendation Pipeline](#core-recommendation-pipeline)
- [📊 Conceptual Data Model](#-conceptual-data-model)
- [🧩 Components and Modules](#-components-and-modules)
- [📁 Proposed Project Structure](#-proposed-project-structure)
- [🌎 Bilingual Architecture — PT-BR / EN](#-bilingual-architecture--pt-br--en)
- [🌐 Web Evolution — Conceptual Routes](#-web-evolution--conceptual-routes)
- [🛠️ Technology Stack](#️-technology-stack)
- [🔄 MVP × Evolution Mapping](#-mvp--evolution-mapping)
- [🛡️ Responsible AI](#️-responsible-ai)
- [🔐 Safety-First Recommendation Logic](#-safety-first-recommendation-logic)
- [⚡ Quick Start](#-quick-start)
- [🚧 Project Status](#-project-status)
- [🌱 Roadmap](#-roadmap)
- [🎼 Project Philosophy](#-project-philosophy)
- [📜 Academic Origin](#-academic-origin)
- [📄 License](#-license)

<br><br>

## 🎯 What is HabitSync?


HabitSync is an **AI agent** that recommends training and diet products — such as supplements, healthy food, and equipment — for **couples**, not just individuals.

Its core differentiator is **dual-profile reconciliation**: it reconciles two people's goals and dietary restrictions simultaneously, always giving **absolute priority to allergies and dietary restrictions** over preferences or goals.

The recommendation engine combines:

- **Content-based filtering**
- A **simulated collaborative-filtering signal**
- A **final weighted ranking**

Every recommendation is accompanied by a bilingual **PT-BR / EN**, human-readable explanation, with optional voice output via **gTTS**.

The project began as an academic case study, **"Assistente Inteligente de Recomendação"**, and is now being evolved into a portfolio-grade AI project.

<br><br>

## 🎼 Music, Meaning & Human-Centered AI

> **Harmony is not becoming the same.  
> It is learning how to move together.**

HabitSync was designed around a simple human idea: two people do not need to have the same goals, habits, routines, preferences, or dietary restrictions to move forward together.

The role of the AI is not to erase those differences.

It is to **understand them, reconcile them, and find meaningful compatibility**.

This concept became part of the project's musical and visual identity through **Bach's Air**.

### 🎼 The Musical Identity

**Air — Johann Sebastian Bach**  
*Orchestral Suite No. 3, BWV 1068*

*Air* is a deeply contemplative work in which different musical lines coexist within a shared harmonic structure.

For HabitSync, it becomes a metaphor:

**Two different lines.  
One shared harmonic space.**

The original movement is titled simply **Air**. The familiar title **Air on the G String** refers to the later arrangement associated with August Wilhelmj.

For the project's contemporary presentation, the chosen recording is:

**Air on the G-String — DEEP HOUSE — REMIX**

The music is not merely background audio. It is part of the project's narrative identity.

> **The music carries the story forward. Take it with you.**

<br><br>

## 🧠 Human-Centered AI

The central question behind HabitSync is:

<br>

> **How can two different people find a shared direction without losing what makes each of them unique?**

<br>

HabitSync approaches that question through AI.

Two people may have:

- different goals;
- different habits;
- different routines;
- different dietary restrictions;
- different preferences;
- different limitations.

The system does not attempt to make their profiles identical.

Instead, it:

**understands → reconciles → evaluates → recommends**

The result is a shared path designed around the realities of both profiles.

<br><br>

# 🏗️ Phase 2 — Complete Architecture: NewVoiceHabits

With Phase 1 approved, HabitSync evolves into **NewVoiceHabits**, the architectural implementation of the recommendation agent.

Phase 2 covers two horizons:

1. **Wednesday MVP** — direct evolution of the existing `assistenteVoz.ipynb`.
2. **Web application evolution** — inspired by the dashboard pattern of the Helipad Detector project, while maintaining completely independent data, models, and business logic.

The Helipad Detector is used only as a **design and architectural inspiration for the presentation layer**. No Helipad data, model, or domain logic is reused.

<br><br>

## 2.1 System Architecture

The system is organized around four main stages:

```text
User / Couple Profiles
        │
        ▼
┌───────────────────────┐
│      Collection       │
│ Goals / Habits /      │
│ Restrictions          │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Recommendation      │
│       Engine          │
│                       │
│ 1. Content-Based      │
│ 2. Collaborative      │
│    Simulated          │
│ 3. Weighted Ranking   │
│ 4. Dual Reconciliation│
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│   Explainability      │
│ Human-readable reason │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Voice Output / UI     │
│ PT-BR / EN            │
└───────────────────────┘


<br><br>



### Architecture Legend

The architecture intentionally distinguishes its computational layers:

* **Purple** — deterministic computational stages such as content filtering and ranking.
* **Coral** — the simulated collaborative stage based on synthetic data, intentionally highlighted so that its non-real origin is immediately visible.
* **Teal** — transparency and explainability layer.

This distinction is especially important for Responsible AI communication and academic presentation.

<br><br>

## 2.2 Core Recommendation Pipeline

The central **Recommendation** block contains the four logical steps required by the original briefing:

### 1. Collection

Collect both profiles:

* goals;
* habits;
* training preferences;
* dietary restrictions;
* constraints.


<br>

### 2. Content

Evaluate product compatibility against the profiles.

### 3. Collaborative — Simulated

Use a synthetic interaction history to simulate collaborative-filtering behavior.

This signal is **not based on real user behavior**.

### 4. Weighted Ranking

Combine the recommendation signals into a final ranking while preserving the underlying scores for transparency.

<br><br>


## 📊 3. Conceptual Data Model

All entities use English identifiers and field names, following the project's coding convention.

All current data is **100% synthetic**.

| Entity           | Main Fields                                                                                          | Description                                                   |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `User`           | `user_id`, `couple_id`, `role`, `goals`, `dietary_restrictions`, `training_type`                     | Each `couple_id` contains exactly two users                   |
| `Product`        | `product_id`, `category`, `subcategory`, `brand`, `price`, `ingredients`, `description`, `tags`      | Example: `protein`, `whey_isolate`, `#vegan`                  |
| `Interaction`    | `interaction_id`, `user_id`, `product_id`, `event_type`, `value`, `timestamp`                        | Synthetic interaction history used by collaborative filtering |
| `Recommendation` | `couple_id`, `product_id`, `content_score`, `collaborative_score`, `final_score`, `explanation_text` | Final pipeline output with explainability                     |

<br><br>

# 🧩 4. Components and Modules

File and function names use English conventions.

Comments and docstrings remain in Portuguese.

```text
voice_output.py

  -> speak(text: str, lang: str) -> None
     # wrapper evolved from the gTTS implementation already used
     # in the original notebook


data_synthetic.py

  -> generate_products(n: int) -> DataFrame

  -> generate_users(n_couples: int) -> DataFrame

  -> generate_interactions(users, products) -> DataFrame
     # simulates collaborative history


recommendation_engine.py

  -> content_based_filter(profile: dict, products: DataFrame) -> DataFrame

  -> simulate_collaborative_filter(
         user_id,
         interactions: DataFrame
     ) -> DataFrame

  -> reconcile_dual_profile(
         profile_a: dict,
         profile_b: dict
     ) -> dict

  -> weighted_rank(
         content_scores,
         collaborative_scores,
         weights: dict
     ) -> DataFrame


explainability.py

  -> explain_recommendation(product, profile) -> str
     # generates the human-readable explanation


conversational_agent.py

  -> parse_command(text: str) -> dict

  -> build_response(
         intent: dict,
         recommendations
     ) -> str
```


<br>

### Conversational Agent

`conversational_agent.py` represents the direct architectural evolution of `processar_comando()` from the original notebook.

Instead of simple rules such as:

```python
if "olá" in comando:
```

<br>

the architecture moves toward structured intent recognition:

```python
{
    "intent": "recommend",
    "goal": "muscle_gain",
    "restriction": "vegan"
}
```

<br>

The philosophy remains the same as the MVP: **text-based simulated commands are sufficient for the initial Wednesday milestone**.

<br><br>

# 📁 5. Proposed Project Structure

```text
newvoicehabits/

├── notebooks/
│   └── newvoicehabits_mvp.ipynb

├── src/
│   ├── voice_output.py
│   ├── data_synthetic.py
│   ├── recommendation_engine.py
│   ├── explainability.py
│   └── conversational_agent.py

├── data/
│   └── synthetic/
│       # generated datasets only — never real data

├── i18n/
│   ├── pt_br.json
│   └── en.json

├── app/
│   └── streamlit_app.py

├── docs/
│   └── relatorio_academico.md

└── README.md
```

<br><br>

## 🌎 6. Bilingual Architecture — PT-BR / EN

HabitSync / NewVoiceHabits uses the same **architectural pattern** adopted by the Helipad Detector application, without reusing its implementation.

The interface uses translation dictionaries:

```text
i18n/
├── pt_br.json
└── en.json
```


<br>

A translation helper such as:

```python
t(key)
```

<br>

is applied only to **interface text**.

Field names and synthetic data remain in English.

### Example

**English**

> Recommended for you: vegan protein isolate, based on your goals and your partner's restrictions.

<br>

**Português (Brasil)**

> Recomendado para vocês: proteína isolada vegana, com base nos objetivos de vocês e nas restrições do seu parceiro/parceira.

<br><br>

# 🌐 7. Web Evolution — Conceptual Routes

The following API routes belong to the future web architecture and are **not implemented in the current MVP**.

| Route                              | Function                                                       |
| ---------------------------------- | -------------------------------------------------------------- |
| `GET /recommendations/{couple_id}` | Returns the current couple ranking                             |
| `POST /preferences/{user_id}`      | Updates goals or restrictions for one partner                  |
| `GET /explain/{product_id}`        | Returns the product explanation                                |
| `POST /voice-command`              | Receives a simulated text command and returns response + audio |

<br><br>

## 🛠️ 8. Technology Stack

| Layer          | MVP — Wednesday                | Web Evolution                        |
| -------------- | ------------------------------ | ------------------------------------ |
| Voice Output   | `gTTS`                         | `gTTS`                               |
| Data           | Synthetic `pandas` in notebook | Same generator served through API    |
| Recommendation | Python / `pandas`              | Same logic encapsulated as a service |
| Interface      | Jupyter Notebook               | Streamlit                            |
| i18n           | Python dictionary              | JSON files by language               |

The future Streamlit application follows the **presentation pattern inspired by the Helipad Detector**, while maintaining independent data, models, and domain logic.

<br><br>

## 🔄 9. MVP × Evolution Mapping

## Wednesday — MVP

The Wednesday milestone consolidates the essential architecture into a single notebook:

```text
voice_output.py
        +
data_synthetic.py
        +
recommendation_engine.py
        +
conversational_agent.py
        ↓
newvoicehabits_mvp.ipynb
```

<br>

The MVP remains intentionally simple and directly evolves the existing `assistenteVoz.ipynb`.

<br><br>

## Web Evolution

The same conceptual modules become decoupled services:

<br>

```text
Frontend / Streamlit
        │
        ▼
API / Application Layer
        │
        ├── Recommendation Engine
        ├── Explainability
        ├── Conversational Agent
        ├── Voice Output
        └── Synthetic Data
```

The future dashboard is planned as a multi-tab application:

* **Recommendations**
* **Couple Profile**
* **Explainability**
* **Governance / Responsible AI**

<br><br>

# 🛡️ 10. Responsible AI

Responsible AI is an architectural requirement, not an optional presentation layer.

### Explainability is mandatory

`explainability.py` is required for every recommendation.

No recommendation should be generated without:

```text
explanation_text
```

### Scores remain transparent

The `Recommendation` entity retains:

```text
content_score
collaborative_score
final_score
```

rather than exposing only a single opaque number.

<br><br>

### Synthetic data is explicitly identified

Every dataset generated by `data_synthetic.py` should carry:

```text
is_synthetic: true
```

This provenance must remain visible in:

* the academic report;
* documentation;
* the future Governance / Responsible AI dashboard.

<br><br>

### No prescriptive nutrition language

Recommendation explanations must use **suggestive product language**, not medical or nutritional prescription language.

The system is an informational recommendation agent.

It is not a replacement for:

* nutrition professionals;
* medical professionals;
* qualified training professionals.

<br><br>

## 🔐 11. Safety-First Recommendation Logic

HabitSync follows a strict priority hierarchy:

<br>

```text
ALLERGIES
    ↓
DIETARY RESTRICTIONS
    ↓
COMPATIBILITY
    ↓
GOALS
    ↓
PREFERENCES
```

Allergies and dietary restrictions have **absolute priority** over preferences or goals.

This principle is central to the dual-profile reconciliation layer.

<br><br>

## ⚡ 12. Quick Start

Clone the repository:

```bash
git clone <this-repo-url>
cd 2-project-ai-agent-habitsync
```

<br>

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

<br>

Generate the synthetic dataset:

```bash
python3 scripts/generate_synthetic_data.py
```

<br>

For the complete beginner-friendly workflow:

```text
execution_guide.md
```

<br>

### Run the MVP

```bash
python3 -m pip install jupyter nbconvert

cd notebooks

jupyter nbconvert --to script habitsync_mvp.ipynb

python3 habitsync_mvp.py
```

<br>

Or open:

```text
notebooks/habitsync_mvp.ipynb
```

<br>


in Google Colab.

<br><br>

# 🚧 13. Project Status

| Phase                                    | Status             |
| ---------------------------------------- | ------------------ |
| Strategic discovery & product definition | ✅ Done             |
| Architecture design                      | ✅ Done             |
| Synthetic dataset                        | ✅ Done & validated |
| MVP notebook                             | ✅ Done & validated |
| Phase 2 architecture                     | ✅ Defined          |
| Professional backend                     | ⏳ In progress      |
| Streamlit web application                | ⏳ In progress      |
| CI/CD                                    | ⏳ Planned          |
| Full documentation                       | ⏳ In progress      |

<br><br>

# 🌱 14. Roadmap

### Phase 1 — Academic MVP

* Recommendation logic
* Synthetic dataset
* Dual-profile reconciliation
* Content-based filtering
* Simulated collaborative filtering
* Weighted ranking
* Explainability
* gTTS voice output
* PT-BR / EN

### Phase 2 — Architecture

* Modular Python architecture
* Structured conversational intents
* Explicit synthetic-data provenance
* Responsible AI layer
* Decoupled recommendation services
* API-oriented design

### Phase 3 — Web Application

* Streamlit dashboard
* Couple profile interface
* Recommendation visualization
* Explainability interface
* Governance / Responsible AI tab
* Voice-command endpoint
* Bilingual interface

### Phase 4 — Production Evolution

* Production-grade backend
* CI/CD
* Deployment architecture
* Expanded evaluation
* Monitoring
* Stronger recommendation infrastructure
* Production-ready documentation

<br><br>

## 🎼 15. Project Philosophy

HabitSync ultimately starts with a simple human observation:

<br>

> **Two lives do not need to follow the same rhythm to move in the same direction.**

<br>

The AI helps find that direction.

Not by erasing differences.

Not by imposing sameness.

But by understanding where different paths can meet.

### **Harmony is not becoming the same.

It is learning how to move together.**

<br><br>

## 🎼 Musical Reference

**Johann Sebastian Bach**
*Air — Orchestral Suite No. 3, BWV 1068*

**Project metaphor:**
*Harmony without sameness.*

**HabitSync philosophy:**
*Different people. Different rhythms. A shared direction.*

<br><br>

##  Academic Origin

HabitSync originated as an academic case study:

<br>

> **Assistente Inteligente de Recomendação**

The project is being evolved into a portfolio-grade AI system focused on:

**AI Agents · Recommendation Systems · Explainable AI · Voice Interfaces · Human-Centered AI · Responsible AI**

<br><br>

## 📄 License

**TBD**

<br><br>

<div align="center">

𝄢

**Air — Johann Sebastian Bach**

*Harmony is not becoming the same.*
*It is learning how to move together.*

**HabitSync — Different people. Different rhythms. A shared direction.**

</div>

<br><br>

## 💌 [Let the data flow... Ping Us]()


- 👩🏻‍🚀 **Fabiana Campanari** - [Shoot me an email](mailto:fabicampanari@proton.me)
  
- 🧑🏼‍🚀 **PedroVyctor** - [Hit me up by email](mailto:pedro.vyctor00@gmail.com)

- 👨🏽‍🚀 **Andson Ribeiro** - [Slide into my inbox]()



<br> 


#### <p align="center">  🛸๋ My Contacts [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center">  ────────────── ⊹🔭๋ ──────────────

<!--
<p align="center">  ────────────── 🛸๋*ੈ✩* 🔭*ੈ₊ ──────────────
-->

<br>

<p align="center"> ➣➢➤ <a href="#top">Back to Top </a>
  
#

##### <p align="center"> Copyright 2024 Mindful-AI-Assistants. Code released under the  [MIT license.](https://github.com/Mindful-AI-Assistants/planet-smart-city-laguna-iot-pucsp/blob/7ac78ed36a9256cbdc0941dbd44fd13b545bc2dd/LICENSE)






