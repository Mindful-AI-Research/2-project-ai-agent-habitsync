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










