import streamlit as st
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils import load_data
df = load_data()

st.set_page_config(page_title="War Economy Dashboard",
                   layout="wide", page_icon="🌍")

st.title("🌍 War Economic Impact Dashboard")
st.markdown("### Complete Analysis of 100,000 Conflict Records (WWII → 2026)")

st.markdown("""
This dashboard analyses the full economic and humanitarian impact of war
across every major conflict in modern history.

Use the **sidebar on the left** to navigate between analysis sections.
""")

st.divider()

st.subheader("📋 What's Inside")

sections = [
    ("📊", "KPI Dashboard",              "Headline numbers — GDP, poverty, unemployment at a glance"),
    ("🗺️", "Conflict Overview",           "Types of wars, regions affected, ongoing vs resolved"),
    ("📉", "GDP Analysis",               "How wars collapse national economies"),
    ("👷", "Unemployment",               "Job losses, youth unemployment, most affected sectors"),
    ("🍞", "Poverty & Food Security",    "Extreme poverty and hunger caused by conflict"),
    ("💸", "Inflation & Currency",       "Hyperinflation and currency devaluation during war"),
    ("🕵️", "Black Market",              "Shadow economies, war profiteering, illegal trade"),
    ("💰", "War vs Reconstruction Cost", "The true financial price of conflict and rebuilding"),
    ("🌍", "Regional Analysis",          "Which regions suffer the most economically"),
    ("📅", "Temporal Analysis",          "How war economics changed across decades"),
    ("🔗", "Correlation Analysis",       "Which indicators predict the worst outcomes"),
    ("✅", "Conclusions",                "10 key insights from the full dataset"),
]

for icon, title, desc in sections:
    col1, col2 = st.columns([1, 6])
    col1.markdown(f"## {icon}")
    col2.markdown(f"**{title}**  \n{desc}")
    st.divider()