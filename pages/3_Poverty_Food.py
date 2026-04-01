import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Poverty & Food", layout="wide", page_icon="🍞")
st.title("🍞 Poverty & Food Insecurity")
st.markdown("""
Extreme poverty means living on less than $2.15 per day.
Food insecurity means not knowing where the next meal comes from.
These are the most visible human consequences of war's economic destruction.
""")

df = load_data()
df['Poverty_Increase'] = df['During_War_Poverty_Rate_%'] - df['Pre_War_Poverty_Rate_%']

col1, col2 = st.columns(2)
with col1:
    st.subheader("Pre-War vs During-War Poverty Rate")
    fig = px.histogram(df, x='Pre_War_Poverty_Rate_%',
                       color_discrete_sequence=['#27ae60'], opacity=0.7)
    fig.add_histogram(x=df['During_War_Poverty_Rate_%'],
                      marker_color='#e74c3c', opacity=0.7, name='During War')
    fig.update_layout(barmode='overlay')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Extreme Poverty vs Food Insecurity")
    fig = px.scatter(
        df.dropna(subset=['Extreme_Poverty_Rate_%', 'Food_Insecurity_Rate_%']).sample(2000),
        x='Extreme_Poverty_Rate_%', y='Food_Insecurity_Rate_%',
        color='Region', opacity=0.5)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Poverty Increase by Region")
data = df.groupby('Region')['Poverty_Increase'].mean().reset_index()
fig = px.bar(data, x='Region', y='Poverty_Increase',
             color='Poverty_Increase', color_continuous_scale='Reds')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Poverty Increase Heatmap — Region vs Conflict Type")
pivot = df.groupby(['Region', 'Conflict_Type'])['Poverty_Increase'].mean().unstack(fill_value=0)
fig2, ax = plt.subplots(figsize=(12, 5))
sns.heatmap(pivot, annot=True, fmt='.1f', cmap='Reds', ax=ax)
ax.set_title('Avg Poverty Increase (%) by Region and Conflict Type')
st.pyplot(fig2)