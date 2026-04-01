import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Inflation & Currency", layout="wide", page_icon="💸")
st.title("💸 Inflation & Currency Devaluation")
st.markdown("""
When governments can't fund war through taxes they print money.
Too much printing causes inflation. Hyperinflation destroys savings overnight.
Currency devaluation makes imports unaffordable for ordinary civilians.
""")

df = load_data()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Inflation Rate Distribution")
    fig = px.histogram(df, x='Inflation_Rate_%', nbins=50,
                       color_discrete_sequence=['#e74c3c'])
    fig.add_vline(x=df['Inflation_Rate_%'].mean(), line_dash='dash',
                  line_color='yellow', annotation_text='Mean')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Currency Devaluation Distribution")
    fig = px.histogram(df, x='Currency_Devaluation_%', nbins=50,
                       color_discrete_sequence=['#e67e22'])
    st.plotly_chart(fig, use_container_width=True)

st.subheader("GDP Collapse vs Inflation")
fig = px.scatter(
    df.dropna(subset=['GDP_Change_%', 'Inflation_Rate_%']).sample(2000),
    x='GDP_Change_%', y='Inflation_Rate_%',
    color='Region',
    hover_name='Primary_Country', opacity=0.5,
    labels={'GDP_Change_%': 'GDP Change (%)', 'Inflation_Rate_%': 'Inflation (%)'})
st.plotly_chart(fig, use_container_width=True)

st.subheader("Average Inflation by Conflict Type")
data = df.groupby('Conflict_Type')['Inflation_Rate_%'].mean().reset_index()
fig = px.bar(data, x='Conflict_Type', y='Inflation_Rate_%',
             color='Inflation_Rate_%', color_continuous_scale='Reds')
st.plotly_chart(fig, use_container_width=True)