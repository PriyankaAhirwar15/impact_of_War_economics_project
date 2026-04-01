import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Unemployment", layout="wide", page_icon="👷")
st.title("👷 Unemployment Analysis")
st.markdown("""
When conflict begins, businesses shut and millions lose jobs overnight.
Youth unemployment is particularly devastating — young people who cannot
find work during wartime rarely fully recover economically.
""")

df = load_data()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Pre-War vs During-War Unemployment")
    fig = px.histogram(df, x='Pre_War_Unemployment_%',
                       color_discrete_sequence=['#27ae60'], opacity=0.7,
                       labels={'Pre_War_Unemployment_%': 'Unemployment (%)'})
    fig.add_histogram(x=df['During_War_Unemployment_%'],
                      marker_color='#e74c3c', opacity=0.7, name='During War')
    fig.update_layout(barmode='overlay')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Unemployment Spike by Region")
    data = df.groupby('Region')['Unemployment_Spike_Percentage_Points'].mean().reset_index()
    fig = px.bar(data, x='Region', y='Unemployment_Spike_Percentage_Points',
                 color='Unemployment_Spike_Percentage_Points',
                 color_continuous_scale='Reds',
                 labels={'Unemployment_Spike_Percentage_Points': 'Spike (pp)'})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Unemployment Spike by Conflict Type")
data2 = df.groupby('Conflict_Type')['Unemployment_Spike_Percentage_Points'].mean().reset_index()
fig = px.bar(data2, x='Conflict_Type', y='Unemployment_Spike_Percentage_Points',
             color='Unemployment_Spike_Percentage_Points',
             color_continuous_scale='Reds')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Most Affected Economic Sectors")
sector = df['Most_Affected_Sector'].value_counts().reset_index()
sector.columns = ['Sector', 'Count']
fig = px.treemap(sector, path=['Sector'], values='Count',
                 color='Count', color_continuous_scale='Reds')
st.plotly_chart(fig, use_container_width=True)

st.subheader("Youth Unemployment Change by Conflict Type")
fig = px.violin(df.dropna(subset=['Youth_Unemployment_Change_%']),
                x='Conflict_Type', y='Youth_Unemployment_Change_%',
                color='Conflict_Type', box=True)
fig.update_layout(showlegend=False)
st.plotly_chart(fig, use_container_width=True)