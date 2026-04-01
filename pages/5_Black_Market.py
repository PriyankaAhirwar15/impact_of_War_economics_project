import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="Black Market", layout="wide", page_icon="🕵️")
st.title("🕵️ Black Markets & Informal Economy")
st.markdown("""
When formal markets collapse during war, black markets fill the vacuum.
They supply food, fuel, medicine and currency when official channels fail —
but concentrate wealth in dangerous hands.
""")

df = load_data()

col1, col2 = st.columns(2)
with col1:
    st.subheader("Informal Economy — Pre vs During War")
    fig = px.histogram(df, x='Informal_Economy_Size_Pre_War_%',
                       color_discrete_sequence=['#27ae60'], opacity=0.7)
    fig.add_histogram(x=df['Informal_Economy_Size_During_War_%'],
                      marker_color='#e74c3c', opacity=0.7, name='During War')
    fig.update_layout(barmode='overlay')
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Black Market Activity Level")
    data = df['Black_Market_Activity_Level'].value_counts().reset_index()
    data.columns = ['Level', 'Count']
    fig = px.pie(data, names='Level', values='Count',
                 color_discrete_sequence=['#e74c3c', '#e67e22', '#f39c12', '#2ecc71'])
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Most Traded Black Market Goods")
goods = df['Primary_Black_Market_Goods'].value_counts().head(12).reset_index()
goods.columns = ['Goods', 'Count']
fig = px.bar(goods, x='Count', y='Goods', orientation='h',
             color='Count', color_continuous_scale='Reds')
st.plotly_chart(fig, use_container_width=True)

st.subheader("War Profiteering by Region")
profit = df.groupby(['Region', 'War_Profiteering_Documented']).size().reset_index(name='Count')
fig = px.bar(profit, x='Count', y='Region',
             color='War_Profiteering_Documented', orientation='h',
             barmode='stack',
             color_discrete_map={'Yes': '#e74c3c', 'No': '#27ae60'})
st.plotly_chart(fig, use_container_width=True)