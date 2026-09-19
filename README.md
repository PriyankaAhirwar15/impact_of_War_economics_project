<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=War%20Economic%20Impact%20Dashboard&fontSize=40&fontColor=fff&animation=fadeIn&fontAlignY=38&desc=Analysing%20100%2C000%20Conflict%20Records%20%7C%20WWII%20→%202026&descAlignY=60&descSize=16" width="100%"/>

<br/>

<!-- Badges Row 1 -->
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32+-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Scikit--Learn](https://img.shields.io/badge/Scikit--Learn-1.4+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-5.0+-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
<br/>
<!-- Badges Row 2 -->
![Status](https://img.shields.io/badge/Status-Active-00C851?style=for-the-badge)
![Records](https://img.shields.io/badge/Records-100%2C000-e74c3c?style=for-the-badge)
![Pages](https://img.shields.io/badge/Dashboard%20Pages-12-9b59b6?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

#### 🔗 **[Click here to Live](https://impactofwareconomicsprojectgit-gep2nly75qeohxj8aef9n9.streamlit.app/)**

<br/><br/>

> **"Behind every war, two battles are fought simultaneously.**
> **The first on the frontlines. The second on the breadlines."**

<br/>

</div>

---

## 📌 Table of Contents

| # | Section |
|---|---------|
| 1 | [🌍 Project Overview](#-project-overview) |
| 2 | [✨ Features](#-features) |
| 3 | [📊 Dashboard Pages](#-dashboard-pages) |
| 4 | [🛠️ Tech Stack](#️-tech-stack) |
| 5 | [📁 Project Structure](#-project-structure) |
| 6 | [⚙️ Installation & Setup](#️-installation--setup) |
| 7 | [🚀 Running the App](#-running-the-app) |
| 8 | [🤖 AI Prediction Model](#-ai-prediction-model) |
| 9 | [📈 Key Insights](#-key-insights) |
| 10 | [🗃️ Dataset](#️-dataset) |
| 11 | [🙌 Acknowledgements](#-acknowledgements) |

---

## 🌍 Project Overview

<div align="center">

```
┌─────────────────────────────────────────────────────────────────┐
│                                                                   │
│   100,000 conflict records  ·  5 regions  ·  WWII → 2026        │
│   28 economic variables  ·  12 analysis modules  ·  1 AI model  │
│                                                                   │
└─────────────────────────────────────────────────────────────────┘
```

</div>

The **War Economic Impact Dashboard** is an industrial-level data analytics platform that analyses the full economic and humanitarian consequences of armed conflict across modern history.

Built with **Python + Streamlit**, it transforms raw conflict data into interactive visualisations, statistical analyses, and AI-powered predictions — making the human cost of war impossible to ignore.

This project covers:
- 💀 **GDP collapses** — how wars destroy national economies
- 📈 **Hyperinflation** — when printing money spins out of control
- 👷 **Mass unemployment** — job destruction and youth economic scars
- 🍞 **Poverty & hunger** — families falling below the poverty line
- 🕵️ **Black markets** — shadow economies and war profiteering
- 💰 **Reconstruction costs** — why rebuilding always costs more than the war

---

## ✨ Features

```
╔══════════════════════════════════════════════════════════════╗
║  FEATURE                          DESCRIPTION                ║
╠══════════════════════════════════════════════════════════════╣
║  12 Analysis Pages                One page per topic         ║
║  Interactive Plotly Charts        Zoom, hover, filter        ║
║  Sidebar Filters                  Region & conflict type     ║
║  Live KPI Cards                   Real-time aggregates       ║
║  Heatmaps & Violin Plots          Statistical depth          ║
║  Choropleth World Map             Geographic impact view     ║
║  AI Reconstruction Predictor      Random Forest ML model     ║
║  Temporal Trend Lines             Decade-by-decade analysis  ║
║  Correlation Matrix               Leading indicator signals  ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📊 Dashboard Pages

<div align="center">

| Icon | Page | What You Will Learn |
|------|------|---------------------|
| 📊 | **KPI Dashboard** | Headline numbers — GDP, poverty, unemployment at a glance |
| 🗺️ | **Conflict Overview** | Types of wars, regions, ongoing vs resolved |
| 📉 | **GDP Analysis** | How wars collapse national economies |
| 👷 | **Unemployment** | Job losses, youth scars, most affected sectors |
| 🍞 | **Poverty & Food Security** | Extreme poverty and hunger caused by conflict |
| 💸 | **Inflation & Currency** | Hyperinflation and currency devaluation |
| 🕵️ | **Black Market** | Shadow economies, illegal trade, war profiteering |
| 💰 | **War vs Reconstruction Cost** | True financial price of conflict and rebuilding |
| 🌍 | **Regional Analysis** | Which regions suffer the most economically |
| 📅 | **Temporal Analysis** | How war economics changed across decades |
| 🔗 | **Correlation Analysis** | Which indicators predict the worst outcomes |
| ✅ | **Conclusions + AI Predictor** | 10 key insights + ML reconstruction cost model |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | Streamlit 1.32+ | Multi-page web dashboard |
| **Data Processing** | Pandas 2.0, NumPy | Data cleaning & feature engineering |
| **Visualisation** | Plotly Express, Seaborn, Matplotlib | Interactive & statistical charts |
| **Machine Learning** | Scikit-learn (Random Forest) | Reconstruction cost prediction |
| **Statistics** | Statsmodels | OLS trendline regression |
| **Language** | Python 3.10+ | Core runtime |

</div>

---

## 📁 Project Structure

```
War_Economic_Project/
│
├── 📄 app.py                          # Home page — navigation & overview
├── 🤖 model.py                        # Random Forest ML model
├── 🔧 utils.py                        # Shared data loader (cached)
├── 📋 requirements.txt                # All dependencies
│
├── 📂 pages/                          # 12 Streamlit dashboard pages
│   ├── 1_GDP_Analysis.py              # GDP collapse analysis
│   ├── 2_Unemployment.py              # Unemployment & sector analysis
│   ├── 3_Poverty_Food.py              # Poverty & food insecurity
│   ├── 4_Inflation_Currency.py        # Inflation & currency devaluation
│   ├── 5_Black_Market.py              # Shadow economy & profiteering
│   ├── 6_War_vs_Reconstruction_Cost.py# Cost comparison analysis
│   ├── 7_Regional_Analysis.py         # Geographic damage heatmap
│   ├── 8_Conflict_Overview.py         # Conflict type & status breakdown
│   ├── 9_Temporal_Analysis.py         # Decade-by-decade trends
│   ├── 10_Correlation_Analysis.py     # Statistical correlation matrix
│   ├── 11_KPI_Dashboard.py            # Live headline KPI cards
│   └── 12_Conclusions.py             # Insights + AI predictor
│
└── 📂 dataset/
    └── war_economic_impact_dataset.csv  # 100,000 conflict records
```

---

## ⚙️ Installation & Setup

### Prerequisites

Make sure you have the following installed:

- ✅ Python 3.10 or higher → [python.org](https://python.org/downloads)
- ✅ VS Code → [code.visualstudio.com](https://code.visualstudio.com)
- ✅ Git (optional) → [git-scm.com](https://git-scm.com)

### Step 1 — Clone or Download the Project

```bash
# Option A — Clone via Git
git clone https://github.com/yourusername/War_Economic_Project.git
cd War_Economic_Project

# Option B — Download ZIP and open folder in VS Code
```

### Step 2 — Create a Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — Mac / Linux
source venv/bin/activate
```

### Step 3 — Install All Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy scikit-learn plotly seaborn matplotlib statsmodels
```

### Step 4 — Add the Dataset

Place the dataset file in the `dataset/` folder:

```
War_Economic_Project/
└── dataset/
    └── war_economic_impact_dataset.csv   ← put it here
```

> **Dataset source:** [Kaggle — War Economic and Livelihood Impact Dataset](https://www.kaggle.com/datasets/likithagedipudi/war-economic-and-livelihood-impact-dataset)

---

## 🚀 Running the App

```bash
streamlit run app.py
```

The dashboard will open automatically at:

```
http://localhost:8501
```

Use the **left sidebar** to navigate between all 12 analysis pages.

---

## 🤖 AI Prediction Model

The dashboard includes a trained **Random Forest Regressor** that predicts reconstruction costs from conflict characteristics.

```
┌─────────────────────────────────────────────────────┐
│              MODEL ARCHITECTURE                      │
│                                                      │
│  INPUT FEATURES                                      │
│  ├── Conflict Type    (encoded)                      │
│  ├── Region           (encoded)                      │
│  ├── GDP Change %                                    │
│  ├── Inflation Rate %                                │
│  └── Unemployment Spike (percentage points)          │
│                                                      │
│  MODEL                                               │
│  └── Random Forest Regressor                         │
│       ├── 100 estimators                             │
│       ├── Train/Test split: 80/20                    │
│       └── Evaluation: Mean Absolute Error ($B)       │
│                                                      │
│  OUTPUT                                              │
│  └── Estimated Reconstruction Cost (USD Billions)    │
└─────────────────────────────────────────────────────┘
```

**How to use it:**
1. Navigate to the **Conclusions** page
2. Select conflict type and region
3. Adjust the GDP, inflation, and unemployment sliders
4. Click **⚡ Predict Reconstruction Cost**

---

## 📈 Key Insights

After analysing 100,000 conflict records, here is what the data reveals:

```
01  GDP COLLAPSE IS UNIVERSAL
    Every conflict type causes significant GDP contraction — no economy is immune.

02  CIVIL WARS ARE MOST DESTRUCTIVE
    They destroy internal infrastructure with no safe zones for economic activity.

03  INFLATION AND GDP COLLAPSE MOVE TOGETHER
    As economies shrink, governments print money — creating a self-reinforcing spiral.

04  RECONSTRUCTION COSTS MORE THAN THE WAR
    Destroying is fast and cheap. Rebuilding is slow and expensive.

05  YOUTH UNEMPLOYMENT CREATES GENERATIONAL SCARS
    Young people who cannot find work during conflict rarely fully recover.

06  BLACK MARKETS GROW WITH FORMAL ECONOMY COLLAPSE
    Shadow economies fill the vacuum but concentrate wealth dangerously.

07  EXTREME POVERTY AND FOOD INSECURITY ARE INSEPARABLE
    They share nearly identical geographic and conflict-type patterns.

08  MIDDLE EAST AND AFRICA SUFFER MOST
    Pre-existing fragility amplifies conflict damage in these regions.

09  LONGER CONFLICTS COMPOUND DAMAGE NON-LINEARLY
    Economic damage does not scale linearly with duration — it compounds.

10  MODERN CONFLICTS SCORE HIGHER SEVERITY
    Global financial interconnection means economic shockwaves spread wider.
```

---

## 🗃️ Dataset

| Property | Value |
|----------|-------|
| **Records** | 100,000 conflict-level rows |
| **Columns** | 28 economic & humanitarian variables |
| **Coverage** | WWII (1939) → Israel-Iran conflict (2026) |
| **Regions** | Africa, East Asia, Europe, Middle East, South Asia |
| **Conflict Types** | Civil War, Interstate War, Asymmetric War, World War, Counter-insurgency |
| **Source** | Kaggle — likithagedipudi |

**Key columns include:**

`GDP_Change_%` · `Inflation_Rate_%` · `Currency_Devaluation_%` · `Unemployment_Spike_Percentage_Points` · `Youth_Unemployment_Change_%` · `Extreme_Poverty_Rate_%` · `Food_Insecurity_Rate_%` · `Cost_of_War_USD` · `Estimated_Reconstruction_Cost_USD` · `Black_Market_Activity_Level` · `War_Profiteering_Documented`

---

## 🙌 Acknowledgements

- 📊 Dataset by [likithagedipudi on Kaggle](https://www.kaggle.com/datasets/likithagedipudi/war-economic-and-livelihood-impact-dataset)
- ⚡ Built with [Streamlit](https://streamlit.io)
- 📈 Charts powered by [Plotly](https://plotly.com)
- 🤖 ML by [Scikit-learn](https://scikit-learn.org)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Made with ❤️ for data, peace, and understanding the true cost of war.**

⭐ Star this repo if it helped you · 🐛 Report issues · 🍴 Fork and build on it

</div>
