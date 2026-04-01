import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Temporal Analysis", layout="wide", page_icon="📅")
st.title("📅 Temporal Analysis — War Economics Over Decades")
st.markdown("""
Cold War conflicts were often funded by superpowers, dampening local damage.
Modern conflicts in interconnected financial systems create wider shockwaves.
Are wars becoming more or less economically devastating over time?
""")

df = load_data()
df['Decade'] = (df['Start_Year'] // 10 * 10).astype(str) + 's'
df['Poverty_Increase'] = df['During_War_Poverty_Rate_%'] - df['Pre_War_Poverty_Rate_%']

decade = df.groupby('Decade').agg(
    Avg_GDP          =('GDP_Change_%', 'mean'),
    Avg_Inflation    =('Inflation_Rate_%', 'mean'),
    Avg_Unemployment =('Unemployment_Spike_Percentage_Points', 'mean'),
    Avg_Poverty      =('Poverty_Increase', 'mean'),
).reset_index()

col1, col2 = st.columns(2)
with col1:
    fig = px.line(decade, x='Decade', y='Avg_GDP',
                  title='Avg GDP Change by Decade', markers=True,
                  color_discrete_sequence=['#e74c3c'])
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.line(decade, x='Decade', y='Avg_Inflation',
                  title='Avg Inflation Rate by Decade', markers=True,
                  color_discrete_sequence=['#e67e22'])
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)
with col3:
    fig = px.line(decade, x='Decade', y='Avg_Unemployment',
                  title='Avg Unemployment Spike by Decade', markers=True,
                  color_discrete_sequence=['#9b59b6'])
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = px.line(decade, x='Decade', y='Avg_Poverty',
                  title='Avg Poverty Increase by Decade', markers=True,
                  color_discrete_sequence=['#c0392b'])
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Number of Conflicts by Start Year")
year_counts = df['Start_Year'].value_counts().sort_index().reset_index()
year_counts.columns = ['Year', 'Count']
fig = px.area(year_counts, x='Year', y='Count',
              color_discrete_sequence=['#e74c3c'])
st.plotly_chart(fig, use_container_width=True)