import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data
from model import train_model, predict_cost

st.set_page_config(page_title="Conclusions", layout="wide", page_icon="✅")
st.title("✅ Key Takeaways & AI Reconstruction Cost Predictor")

st.subheader("📌 10 Key Insights from 100,000 Records")
insights = [
    ("GDP collapse is universal",                    "Every conflict type causes significant GDP contraction — no economy is immune."),
    ("Civil wars are most destructive",              "They destroy internal infrastructure with no safe zones for economic activity."),
    ("Inflation and GDP collapse move together",     "As economies shrink, governments print money — creating a self-reinforcing spiral."),
    ("Reconstruction costs more than the war",       "Destroying is fast and cheap. Rebuilding is slow and expensive."),
    ("Youth unemployment creates generational scars","Young people who can't find work during conflict rarely fully recover."),
    ("Black markets grow with formal collapse",      "Shadow economies fill the vacuum but concentrate wealth dangerously."),
    ("Extreme poverty and food insecurity are inseparable", "They share nearly identical geographic and conflict-type patterns."),
    ("Middle East and Africa suffer most",           "Pre-existing fragility amplifies conflict damage in these regions."),
    ("Longer conflicts compound damage",             "Economic damage does not scale linearly with duration — it compounds."),
    ("Modern conflicts score higher severity",       "Global financial interconnection means shockwaves spread faster and wider."),
]

for i, (title, desc) in enumerate(insights, 1):
    st.markdown(f"**{i}. {title}** — {desc}")

st.divider()
st.subheader("🔮 AI Reconstruction Cost Predictor")
st.markdown("Trained on 100,000 records. Adjust values below to predict reconstruction cost.")

df = load_data()

with st.spinner("Training AI model on 100,000 records..."):
    model, le_type, le_region, mae = train_model(df)
st.caption(f"Model ready — Mean Absolute Error: ${mae/1e9:.2f}B")

p1, p2 = st.columns(2)
c_type   = p1.selectbox("Conflict Type", le_type.classes_)
c_region = p2.selectbox("Region", le_region.classes_)

p3, p4, p5 = st.columns(3)
c_gdp   = p3.slider("GDP Change (%)", -80, 10, -20)
c_inf   = p4.slider("Inflation Rate (%)", 0, 500, 30)
c_unemp = p5.slider("Unemployment Spike (%)", 0, 60, 15)

if st.button("⚡ Predict Reconstruction Cost", type="primary"):
    result = predict_cost(model, le_type, le_region,
                          c_type, c_region, c_gdp, c_inf, c_unemp)
    st.success(f"💰 Estimated Reconstruction Cost: **${result/1e9:.2f} Billion USD**")
    if result > 500e9:
        st.warning("⚠️ Extremely high — indicative of prolonged civil conflict.")