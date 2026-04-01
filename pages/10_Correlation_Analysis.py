import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Correlation Analysis", layout="wide", page_icon="🔗")
st.title("🔗 Correlation & Statistical Analysis")
st.markdown("""
Which economic variables move together during conflict?
Understanding these correlations helps predict which crises follow
from early warning signs — enabling faster humanitarian response.
""")

df = load_data()

corr_cols = ['GDP_Change_%', 'Inflation_Rate_%', 'Currency_Devaluation_%',
             'Unemployment_Spike_Percentage_Points', 'Youth_Unemployment_Change_%',
             'Extreme_Poverty_Rate_%', 'Food_Insecurity_Rate_%',
             'Informal_Economy_Size_During_War_%', 'Currency_Black_Market_Rate_Gap_%']

corr = df[corr_cols].corr()

st.subheader("Correlation Heatmap — Key Economic Indicators")
fig1, ax = plt.subplots(figsize=(12, 8))
sns.heatmap(corr, annot=True, fmt='.2f', cmap='RdYlGn',
            center=0, ax=ax, square=True)
st.pyplot(fig1)

st.divider()
st.subheader("Unemployment Spike by Conflict Type")
fig = px.violin(df, x='Conflict_Type',
                y='Unemployment_Spike_Percentage_Points',
                color='Conflict_Type', box=True)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)