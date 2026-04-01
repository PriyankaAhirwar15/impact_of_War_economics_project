import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="GDP Analysis", layout="wide", page_icon="📉")
st.title("📉 GDP & Macroeconomic Collapse")
st.markdown("""
GDP is the total value of everything a country produces in a year.
During wars it doesn't just slow — it collapses. Factories close,
supply chains break, and foreign investment disappears overnight.
""")

df = load_data()

col1, col2 = st.columns(2)
with col1:
    st.subheader("GDP Change Distribution")
    fig = px.histogram(df, x='GDP_Change_%', nbins=50,
                       color_discrete_sequence=['#e74c3c'],
                       labels={'GDP_Change_%': 'GDP Change (%)'})
    fig.add_vline(x=0, line_dash='dash', line_color='white')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Avg GDP Change by Conflict Type")
    data = df.groupby('Conflict_Type')['GDP_Change_%'].mean().reset_index()
    fig = px.bar(data, x='Conflict_Type', y='GDP_Change_%',
                 color='GDP_Change_%', color_continuous_scale='RdYlGn')
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Avg GDP Change by Region")
data = df.groupby('Region')['GDP_Change_%'].mean().sort_values().reset_index()
fig = px.bar(data, x='GDP_Change_%', y='Region', orientation='h',
             color='GDP_Change_%', color_continuous_scale='RdYlGn')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Does Longer War Mean Worse GDP Damage?")
df2 = df.copy()
df2['Conflict_Duration'] = df2['End_Year'].fillna(2026) - df2['Start_Year']
fig = px.scatter(df2.dropna(subset=['GDP_Change_%', 'Conflict_Duration']),
                 x='Conflict_Duration', y='GDP_Change_%',
                 color='Region', hover_name='Conflict_Name',
                 opacity=0.5,
                 labels={'Conflict_Duration': 'Duration (Years)',
                         'GDP_Change_%': 'GDP Change (%)'})
st.plotly_chart(fig, use_container_width=True)