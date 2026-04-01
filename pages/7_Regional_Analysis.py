import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Regional Analysis", layout="wide", page_icon="🌍")
st.title("🌍 Regional Analysis — Which Regions Suffer Most?")
st.markdown("""
Geography amplifies economic damage. Regions with weak institutions
and resource-dependent economies suffer far more than resilient ones.
""")

df = load_data()
df['Poverty_Increase'] = df['During_War_Poverty_Rate_%'] - df['Pre_War_Poverty_Rate_%']

regional = df.groupby('Region').agg(
    Avg_GDP_Change      =('GDP_Change_%', 'mean'),
    Avg_Inflation       =('Inflation_Rate_%', 'mean'),
    Avg_Unemp_Spike     =('Unemployment_Spike_Percentage_Points', 'mean'),
    Avg_Extreme_Poverty =('Extreme_Poverty_Rate_%', 'mean'),
    Avg_Food_Insecurity =('Food_Insecurity_Rate_%', 'mean'),
).round(2)

st.subheader("Regional Economic Damage Heatmap")
fig1, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(regional, annot=True, fmt='.1f', cmap='Reds', ax=ax)
ax.set_title('Average Economic Indicators by Region')
st.pyplot(fig1)

st.divider()
col1, col2 = st.columns(2)
with col1:
    st.subheader("GDP Change by Region")
    fig = px.bar(regional.reset_index(), x='Region', y='Avg_GDP_Change',
                 color='Avg_GDP_Change', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Food Insecurity by Region")
    fig = px.bar(regional.reset_index(), x='Region', y='Avg_Food_Insecurity',
                 color='Avg_Food_Insecurity', color_continuous_scale='Reds')
    st.plotly_chart(fig, use_container_width=True)