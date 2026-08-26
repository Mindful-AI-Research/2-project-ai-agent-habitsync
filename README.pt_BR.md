\[[**[🇧🇷 Português](README.pt_BR.md)**]\] \[[🇺🇸 English](README.md)\]


<br><br>

# 🎼 HabitSync — Agente de Recomendação com IA - [EXPLORATÓRIO]()
### **Um agente de IA que oferece recomendações explicáveis, guiadas por voz, de produtos para treino e alimentação para casais.**

<br><br>

> 🚧 **MVP acadêmico — validado.** A documentação completa de nível de produção, o backend e a aplicação web fazem parte de um roteiro ativo e faseado.

<br><br>

<!-- ========= START SPONSOR BADGE ========= -->
<p align="center">
  <a href="https://github.com/sponsors/Mindful-AI-Research">
    <img src="https://img.shields.io/badge/Sponsor-%E0%A5%90%20%E2%8B%86%20Mindful%20AI%20%E2%8B%86%20Research%20%26%20Consulting%20%F0%96%A4%90%20%E2%8B%86-00FFFF?style=for-the-badge&logo=githubsponsors&logoColor=white&labelColor=0a1f44" alt="Patrocine ॐ ⋆ Mindful AI ⋆ Pesquisa & Consultoria 𖤐 ⋆">
  </a>
</p>


<br><br>
<!-- ========= END SPONSOR BADGE ========= -->

<!-- =========  START PUC HEADER GIF ========= -->
<p align="center">
   <img src="https://github.com/user-attachments/assets/791a69e2-d09a-429f-9257-f6667fff5c04 ">
 </p>

<br><br>
<!-- =========  END PUC HEADER GIF ========= -->

<!-- ======================================= Start Institucional INFOR =========================================== -->
[**Instituição:**]() Pontifícia Universidade Católica de São Paulo (PUC-SP)  <br>
[**Escola:**]() FACEI — Departamento de Ciência da Computação  <br>
[**Curso:**]() Bacharelado em IA Centrada no Humano e Ciência de Dados • 6º semestre • 2026 <br>
[**Disciplina:**](): Sistemas de Conhecimento em Inteligência Artificial e Agentes Inteligentes  <br>
**Profa. Dra.:** ✨ [Sandra Muniz Bozolan]() <br>
**Autora:** [Fabiana ⚡️ Campanari](https://linktr.ee/fabianacampanari)  

<br><br>

#

<br><br>
<!-- ======================================= SZEnd Institutional INFO ===========================================  -->

<!-- ========= START!WARNING ========= -->
> [!WARNING]
>
> ⚠️ Projetos podem ser compartilhados publicamente quando permitido.  
> O foco está no aprendizado aplicado e prático com conjuntos de dados reais em contextos de governança e segurança de IA.  
> Todo conteúdo sensível permanece protegido em repositórios privados quando necessário.
>

<br><br>

#

<br><br>
<!-- ========= END!WARNING ========= -->


<!-- ========= START APP BADGE ========= -->
<p align="center" style="margin: 0;">
  <a href="https://effulgent-banoffee-ed032c.netlify.app/" rel="noopener noreferrer">
    <img 
      src="https://img.shields.io/badge/Live%20App-HabitSync-0f172a?style=for-the-badge&logo=netlify&logoColor=white" 
      alt="Aplicação HabitSync ao vivo"
      style="height: 38px; width: auto;"
    />
  </a>
</p>
<!-- ========= END APP BADGE ========= -->

<br><br>

## 📚 Sumário

- [🎯 O que é o HabitSync?](#-o-que-é-o-habitsync)
- [🎼 Música, Significado e IA Centrada no Humano](#-música-significado-e-ia-centrada-no-humano)
  - [🎼 A Identidade Musical](#-a-identidade-musical)
  - [🧠 IA Centrada no Humano](#-ia-centrada-no-humano)
  - [✨ A Mensagem Central](#-a-mensagem-central)
- [🔍 Como Funciona o Mecanismo de Recomendação](#-como-funciona-o-mecanismo-de-recomendação)
- [🏗️ Fase 2 — Arquitetura Completa: NewVoiceHabits](#️-fase-2--arquitetura-completa-newvoicehabits)
  - [Arquitetura do Sistema](#arquitetura-do-sistema)
  - [Pipeline Central de Recomendação](#pipeline-central-de-recomendação)
- [📊 Modelo de Dados Conceitual](#-modelo-de-dados-conceitual)
- [🧩 Componentes e Módulos](#-componentes-e-módulos)
- [📁 Estrutura Proposta do Projeto](#-estrutura-proposta-do-projeto)
- [🌎 Arquitetura Bilíngue — PT-BR / EN](#-arquitetura-bilíngue--pt-br--en)
- [🌐 Evolução Web — Rotas Conceituais](#-evolução-web--rotas-conceituais)
- [🛠️ Stack de Tecnologia](#️-stack-de-tecnologia)
- [🔄 Mapeamento MVP × Evolução](#-mapeamento-mvp--evolução)
- [🛡️ IA Responsável](#️-ia-responsável)
- [🔐 Lógica de Recomendação com Segurança em Primeiro Lugar](#-lógica-de-recomendação-com-segurança-em-primeiro-lugar)
- [⚡ Início Rápido](#-início-rápido)
- [🚧 Status do Projeto](#-status-do-projeto)
- [🌱 Roteiro](#-roteiro)
- [🎼 Filosofia do Projeto](#-filosofia-do-projeto)
- [📜 Origem Acadêmica](#-origem-acadêmica)
- [📄 Licença](#-licença)

<br><br>

## 🎯 O que é o HabitSync?

HabitSync é um **agente de IA** que recomenda produtos para treino e alimentação — como suplementos, alimentos saudáveis e equipamentos — para **casais**, e não apenas para indivíduos.

Seu principal diferencial é a **reconciliação de dois perfis**: ele concilia simultaneamente os objetivos e as restrições alimentares de duas pessoas, sempre dando **prioridade absoluta a alergias e restrições alimentares** em relação a preferências ou objetivos.

O mecanismo de recomendação combina:

- **Filtragem baseada em conteúdo**
- Um **sinal simulado de filtragem colaborativa**
- Um **ranqueamento final ponderado**

Cada recomendação é acompanhada de uma explicação bilíngue **PT-BR / EN**, legível por humanos, com saída de voz opcional por meio do **gTTS**.

O projeto começou como um estudo de caso acadêmico, **"Assistente Inteligente de Recomendação"**, e agora está evoluindo para um projeto de IA de nível portfólio.

<br><br>

## 🎼 Música, Significado e IA Centrada no Humano

> **Harmonia não é tornar-se igual.  
> É aprender a se mover juntos.**

O HabitSync foi concebido a partir de uma ideia humana simples: duas pessoas não precisam ter os mesmos objetivos, hábitos, rotinas, preferências ou restrições alimentares para avançarem juntas.

O papel da IA não é apagar essas diferenças.

É **compreendê-las, conciliá-las e encontrar uma compatibilidade significativa**.

Esse conceito se tornou parte da identidade musical e visual do projeto por meio de **Air, de Bach**.

### 🎼 A Identidade Musical

**Air — Johann Sebastian Bach**  
*Suíte Orquestral nº 3, BWV 1068*

*Air* é uma obra profundamente contemplativa, na qual diferentes linhas musicais coexistem em uma estrutura harmônica compartilhada.

Para o HabitSync, ela se torna uma metáfora:

**Duas linhas diferentes.  
Um espaço harmônico compartilhado.**

O movimento original se chama simplesmente **Air**. O título conhecido **Air on the G String** refere-se ao arranjo posterior associado a August Wilhelmj.

Para a apresentação contemporânea do projeto, a gravação escolhida é:

**Air on the G-String — DEEP HOUSE — REMIX**

A música não é apenas áudio de fundo. Ela faz parte da identidade narrativa do projeto.

> **A música conduz a história adiante. Leve-a com você.**

<br><br>

## 🧠 IA Centrada no Humano

A questão central por trás do HabitSync é:

<br>

> **Como duas pessoas diferentes podem encontrar uma direção compartilhada sem perder o que torna cada uma única?**

<br>

O HabitSync aborda essa questão por meio da IA.

Duas pessoas podem ter:

- objetivos diferentes;
- hábitos diferentes;
- rotinas diferentes;
- restrições alimentares diferentes;
- preferências diferentes;
- limitações diferentes.

O sistema não tenta tornar os perfis idênticos.

Em vez disso, ele:

**compreende → concilia → avalia → recomenda**

O resultado é um caminho compartilhado, projetado em torno da realidade de ambos os perfis.

<br><br>

# 🏗️ Fase 2 — Arquitetura Completa: NewVoiceHabits

Com a Fase 1 aprovada, o HabitSync evolui para **NewVoiceHabits**, a implementação arquitetural do agente de recomendação.

A Fase 2 abrange dois horizontes:

1. **MVP de quarta-feira** — evolução direta do `assistenteVoz.ipynb` existente.
2. **Evolução para aplicação web** — inspirada no padrão de dashboard do projeto Helipad Detector, mantendo dados, modelos e lógica de negócio totalmente independentes.

O Helipad Detector é utilizado apenas como **inspiração de design e arquitetura para a camada de apresentação**. Nenhum dado, modelo ou lógica de domínio do Helipad é reutilizado.

<br><br>

## 2.1 Arquitetura do Sistema

O sistema é organizado em quatro estágios principais:

```text
Perfis de Usuários / Casal
        │
        ▼
┌───────────────────────┐
│       Coleta          │
│ Metas / Hábitos /     │
│ Restrições            │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Mecanismo de       │
│    Recomendação       │
│                       │
│ 1. Baseado em Conteúdo│
│ 2. Colaborativo       │
│    Simulado           │
│ 3. Ranking Ponderado  │
│ 4. Reconciliação Dupla│
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│    Explicabilidade    │
│ Motivo legível por    │
│ humanos               │
└───────────┬───────────┘
            │
            ▼
┌───────────────────────┐
│ Saída de Voz / UI     │
│ PT-BR / EN            │
└───────────────────────┘
```

<br><br>

### Legenda da Arquitetura

A arquitetura distingue intencionalmente suas camadas computacionais:

* **Roxo** — estágios computacionais determinísticos, como filtragem de conteúdo e ranqueamento.
* **Coral** — estágio colaborativo simulado com base em dados sintéticos, destacado intencionalmente para que sua origem não real seja imediatamente visível.
* **Verde-azulado** — camada de transparência e explicabilidade.

Essa distinção é especialmente importante para a comunicação de IA Responsável e para a apresentação acadêmica.

<br><br>

## 2.2 Pipeline Central de Recomendação

O bloco central de **Recomendação** contém as quatro etapas lógicas exigidas pelo briefing original:

### 1. Coleta

Coleta ambos os perfis:

* objetivos;
* hábitos;
* preferências de treino;
* restrições alimentares;
* limitações.

<br>

### 2. Conteúdo

Avalia a compatibilidade dos produtos com os perfis.

### 3. Colaborativo — Simulado

Usa um histórico sintético de interações para simular o comportamento da filtragem colaborativa.

Esse sinal **não é baseado no comportamento de usuários reais**.

### 4. Ranqueamento Ponderado

Combina os sinais de recomendação em um ranking final, preservando os escores subjacentes para transparência.

<br><br>

## 📊 3. Modelo de Dados Conceitual

Todas as entidades usam identificadores e nomes de campos em inglês, seguindo a convenção de código do projeto.

Todos os dados atuais são **100% sintéticos**.

| Entidade | Campos Principais | Descrição |
| ---------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| `User` | `user_id`, `couple_id`, `role`, `goals`, `dietary_restrictions`, `training_type` | Cada `couple_id` contém exatamente dois usuários |
| `Product` | `product_id`, `category`, `subcategory`, `brand`, `price`, `ingredients`, `description`, `tags` | Exemplo: `protein`, `whey_isolate`, `#vegan` |
| `Interaction` | `interaction_id`, `user_id`, `product_id`, `event_type`, `value`, `timestamp` | Histórico sintético de interações usado pela filtragem colaborativa |
| `Recommendation` | `couple_id`, `product_id`, `content_score`, `collaborative_score`, `final_score`, `explanation_text` | Saída final do pipeline com explicabilidade |

<br><br>

# 🧩 4. Componentes e Módulos

Os nomes de arquivos e funções usam convenções em inglês.

Comentários e docstrings permanecem em português.

```text
voice_output.py

  -> speak(text: str, lang: str) -> None
     # wrapper evoluído a partir da implementação de gTTS já utilizada
     # no notebook original


data_synthetic.py

  -> generate_products(n: int) -> DataFrame

  -> generate_users(n_couples: int) -> DataFrame

  -> generate_interactions(users, products) -> DataFrame
     # simula o histórico colaborativo


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
     # gera a explicação legível por humanos


conversational_agent.py

  -> parse_command(text: str) -> dict

  -> build_response(
         intent: dict,
         recommendations
     ) -> str
```

<br>

### Agente Conversacional

`conversational_agent.py` representa a evolução arquitetural direta de `processar_comando()` do notebook original.

Em vez de regras simples como:

```python
if "olá" in comando:
```

<br>

a arquitetura evolui para o reconhecimento estruturado de intenções:

```python
{
    "intent": "recommend",
    "goal": "muscle_gain",
    "restriction": "vegan"
}
```

<br>

A filosofia permanece a mesma do MVP: **comandos simulados baseados em texto são suficientes para o marco inicial de quarta-feira**.

<br><br>

# 📁 5. Estrutura Proposta do Projeto

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
│       # apenas conjuntos de dados gerados — nunca dados reais

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

## 🌎 6. Arquitetura Bilíngue — PT-BR / EN

HabitSync / NewVoiceHabits usa o mesmo **padrão arquitetural** adotado pela aplicação Helipad Detector, sem reutilizar sua implementação.

A interface usa dicionários de tradução:

```text
i18n/
├── pt_br.json
└── en.json
```

<br>

Um helper de tradução como:

```python
t(key)
```

<br>

é aplicado apenas ao **texto da interface**.

Os nomes dos campos e os dados sintéticos permanecem em inglês.

### Exemplo

**English**

> Recommended for you: vegan protein isolate, based on your goals and your partner's restrictions.

<br>

**Português (Brasil)**

> Recomendado para vocês: proteína isolada vegana, com base nos objetivos de vocês e nas restrições do seu parceiro/parceira.

<br><br>

# 🌐 7. Evolução Web — Rotas Conceituais

As rotas de API a seguir pertencem à futura arquitetura web e **não estão implementadas no MVP atual**.

| Rota | Função |
| ---------------------------------- | -------------------------------------------------------------- |
| `GET /recommendations/{couple_id}` | Retorna o ranking atual do casal |
| `POST /preferences/{user_id}` | Atualiza objetivos ou restrições de um dos parceiros |
| `GET /explain/{product_id}` | Retorna a explicação do produto |
| `POST /voice-command` | Recebe um comando de texto simulado e retorna resposta + áudio |

<br><br>

## 🛠️ 8. Stack de Tecnologia

| Camada | MVP — Quarta-feira | Evolução Web |
| -------------- | ------------------------------ | ------------------------------------ |
| Saída de Voz | `gTTS` | `gTTS` |
| Dados | `pandas` sintético no notebook | Mesmo gerador servido pela API |
| Recomendação | Python / `pandas` | Mesma lógica encapsulada como serviço |
| Interface | Jupyter Notebook | Streamlit |
| i18n | Dicionário Python | Arquivos JSON por idioma |

A futura aplicação Streamlit segue o **padrão de apresentação inspirado pelo Helipad Detector**, mantendo dados, modelos e lógica de domínio independentes.

<br><br>

## 🔄 9. Mapeamento MVP × Evolução

## Quarta-feira — MVP

O marco de quarta-feira consolida a arquitetura essencial em um único notebook:

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

O MVP permanece intencionalmente simples e evolui diretamente do `assistenteVoz.ipynb` existente.

<br><br>

## Evolução Web

Os mesmos módulos conceituais tornam-se serviços desacoplados:

<br>

```text
Frontend / Streamlit
        │
        ▼
API / Camada de Aplicação
        │
        ├── Mecanismo de Recomendação
        ├── Explicabilidade
        ├── Agente Conversacional
        ├── Saída de Voz
        └── Dados Sintéticos
```

O futuro dashboard está planejado como uma aplicação com múltiplas abas:

* **Recomendações**
* **Perfil do Casal**
* **Explicabilidade**
* **Governança / IA Responsável**

<br><br>

# 🛡️ 10. IA Responsável

A IA Responsável é um requisito arquitetural, não uma camada opcional de apresentação.

### A explicabilidade é obrigatória

`explainability.py` é obrigatório para cada recomendação.

Nenhuma recomendação deve ser gerada sem:

```text
explanation_text
```

### Os escores permanecem transparentes

A entidade `Recommendation` mantém:

```text
content_score
collaborative_score
final_score
```

em vez de expor apenas um número opaco.

<br><br>

### Os dados sintéticos são identificados explicitamente

Cada conjunto de dados gerado por `data_synthetic.py` deve conter:

```text
is_synthetic: true
```

Essa procedência deve permanecer visível em:

* relatório acadêmico;
* documentação;
* futuro dashboard de Governança / IA Responsável.

<br><br>

### Sem linguagem nutricional prescritiva

As explicações de recomendação devem usar **linguagem sugestiva sobre produtos**, e não prescrição médica ou nutricional.

O sistema é um agente de recomendação informativo.

Ele não substitui:

* profissionais de nutrição;
* profissionais médicos;
* profissionais qualificados de treinamento.

<br><br>

## 🔐 11. Lógica de Recomendação com Segurança em Primeiro Lugar

O HabitSync segue uma hierarquia de prioridade rigorosa:

<br>

```text
ALERGIAS
    ↓
RESTRIÇÕES ALIMENTARES
    ↓
COMPATIBILIDADE
    ↓
OBJETIVOS
    ↓
PREFERÊNCIAS
```

Alergias e restrições alimentares têm **prioridade absoluta** sobre preferências ou objetivos.

Esse princípio é central para a camada de reconciliação de dois perfis.

<br><br>

## ⚡ 12. Início Rápido

Clone o repositório:

```bash
git clone <this-repo-url>
cd 2-project-ai-agent-habitsync
```

<br>

Instale as dependências:

```bash
python3 -m pip install -r requirements.txt
```

<br>

Gere o conjunto de dados sintéticos:

```bash
python3 scripts/generate_synthetic_data.py
```

<br>

Para o fluxo completo e amigável para iniciantes:

```text
execution_guide.md
```

<br>

### Execute o MVP

```bash
python3 -m pip install jupyter nbconvert

cd notebooks

jupyter nbconvert --to script habitsync_mvp.ipynb

python3 habitsync_mvp.py
```

<br>

Ou abra:

```text
notebooks/habitsync_mvp.ipynb
```

<br>

no Google Colab.

<br><br>

# 🚧 13. Status do Projeto

| Fase | Status |
| ---------------------------------------- | ------------------ |
| Descoberta estratégica e definição do produto | ✅ Concluída |
| Design da arquitetura | ✅ Concluída |
| Conjunto de dados sintéticos | ✅ Concluído e validado |
| Notebook MVP | ✅ Concluído e validado |
| Arquitetura da Fase 2 | ✅ Definida |
| Backend profissional | ⏳ Em andamento |
| Aplicação web em Streamlit | ⏳ Em andamento |
| CI/CD | ⏳ Planejado |
| Documentação completa | ⏳ Em andamento |

<br><br>

# 🌱 14. Roteiro

### Fase 1 — MVP Acadêmico

* Lógica de recomendação
* Conjunto de dados sintéticos
* Reconciliação de dois perfis
* Filtragem baseada em conteúdo
* Filtragem colaborativa simulada
* Ranqueamento ponderado
* Explicabilidade
* Saída de voz com gTTS
* PT-BR / EN

### Fase 2 — Arquitetura

* Arquitetura Python modular
* Intenções conversacionais estruturadas
* Procedência explícita de dados sintéticos
* Camada de IA Responsável
* Serviços de recomendação desacoplados
* Design orientado a API

### Fase 3 — Aplicação Web

* Dashboard Streamlit
* Interface de perfil do casal
* Visualização de recomendações
* Interface de explicabilidade
* Aba de Governança / IA Responsável
* Endpoint de comando de voz
* Interface bilíngue

### Fase 4 — Evolução para Produção

* Backend de nível de produção
* CI/CD
* Arquitetura de implantação
* Avaliação ampliada
* Monitoramento
* Infraestrutura de recomendação mais robusta
* Documentação pronta para produção

<br><br>

## 🎼 15. Filosofia do Projeto

O HabitSync começa, em última instância, com uma simples observação humana:

<br>

> **Duas vidas não precisam seguir o mesmo ritmo para se moverem na mesma direção.**

<br>

A IA ajuda a encontrar essa direção.

Não apagando as diferenças.

Não impondo uniformidade.

Mas compreendendo onde caminhos diferentes podem se encontrar.

### **Harmonia não é tornar-se igual.

É aprender a se mover juntos.**

<br><br>

## 🎼 Referência Musical

**Johann Sebastian Bach**
*Air — Suíte Orquestral nº 3, BWV 1068*

**Metáfora do projeto:**
*Harmonia sem uniformidade.*

**Filosofia do HabitSync:**
*Pessoas diferentes. Ritmos diferentes. Uma direção compartilhada.*

<br><br>

## Origem Acadêmica

O HabitSync surgiu como um estudo de caso acadêmico:

<br>

> **Assistente Inteligente de Recomendação**

O projeto está evoluindo para um sistema de IA de nível portfólio, focado em:

**Agentes de IA · Sistemas de Recomendação · IA Explicável · Interfaces de Voz · IA Centrada no Humano · IA Responsável**

<br><br>

## 📄 Licença

**A definir**

<br><br>

<div align="center">

𝄢

**Air — Johann Sebastian Bach**

*Harmonia não é tornar-se igual.*
*É aprender a se mover juntos.*

**HabitSync — Pessoas diferentes. Ritmos diferentes. Uma direção compartilhada.**

</div>

<br><br>

## 💌 [Deixe os dados fluírem... Fale com a gente]()


- 👩🏻‍🚀 **Fabiana Campanari** - [Envie-me um e-mail](mailto:fabicampanari@proton.me)
  
- 🧑🏼‍🚀 **PedroVyctor** - [Fale comigo por e-mail](mailto:pedro.vyctor00@gmail.com)

- 👨🏽‍🚀 **Andson Ribeiro** - [Entre em contato]()... <br> 


#### <p align="center"> 🛸๋ Meus contatos [Hub](https://linktr.ee/fabianacampanari)


<br>

### <p align="center"> <img src="https://github.com/user-attachments/assets/517fc573-7607-4c5d-82a7-38383cc0537d" />


<br><br>

<p align="center"> ────────────── ⊹🔭๋ ──────────────

<!--
<p align="center"> ────────────── 🛸๋*ੈ✩* 🔭*ੈ₊ ──────────────
-->

<br>

<p align="center"> ➣➢➤ <a href="#top">Voltar ao topo</a>
  
#

##### <p align="center"> Copyright 2024 Mindful-AI-Assistants. Código disponibilizado sob a [licença MIT.](https://github.com/Mindful-AI-Assistants/planet-smart-city-laguna-iot-pucsp/blob/7ac78ed36a9256cbdc0941dbd44fd13b545bc2dd/LICENSE)
