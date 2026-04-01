import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Conflict Overview", layout="wide", page_icon="🗺️")
st.title("🗺️ Conflict Overview — Types, Regions & Status")
st.markdown("""
Not all wars are the same. Civil wars, interstate conflicts, and asymmetric wars
each destroy economies differently. This maps the full composition of the dataset.
""")

df = load_data()

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Conflict Types")
    fig = px.pie(df, names='Conflict_Type', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Regional Distribution")
    fig = px.pie(df, names='Region', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col3:
    st.subheader("Conflict Status")
    fig = px.pie(df, names='Status', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

st.subheader("🌍 Countries by Number of Conflict Records")
country_data = df['Primary_Country'].value_counts().reset_index()
country_data.columns = ['Country', 'Count']
fig = px.choropleth(country_data, locations='Country',
                    locationmode='country names',
                    color='Count', color_continuous_scale='Reds',
                    title='Conflict Records by Country')
st.plotly_chart(fig, use_container_width=True)