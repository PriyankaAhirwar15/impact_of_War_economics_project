import streamlit as st
import pandas as pd
import plotly.express as px
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="War vs Reconstruction Cost", layout="wide", page_icon="💰")
st.title("💰 Cost of War vs Reconstruction Cost")
st.markdown("""
Destroying is fast and cheap. Rebuilding is slow and expensive.
Reconstruction almost always costs more than the war itself.
""")

df = load_data()
df2 = df.dropna(subset=['Cost_of_War_USD', 'Estimated_Reconstruction_Cost_USD']).copy()
df2['War_Cost_B']   = df2['Cost_of_War_USD'] / 1e9
df2['Recon_Cost_B'] = df2['Estimated_Reconstruction_Cost_USD'] / 1e9
df2['Recon_Ratio']  = df2['Recon_Cost_B'] / df2['War_Cost_B'].replace(0, 1)

col1, col2 = st.columns(2)
with col1:
    st.subheader("War Cost vs Reconstruction Cost (log scale)")
    fig = px.scatter(df2.sample(min(3000, len(df2))),
                     x='War_Cost_B', y='Recon_Cost_B',
                     color='Region', hover_name='Conflict_Name',
                     log_x=True, log_y=True, opacity=0.6,
                     labels={'War_Cost_B': 'War Cost ($B)',
                             'Recon_Cost_B': 'Reconstruction Cost ($B)'})
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Reconstruction-to-War Cost Ratio")
    fig = px.histogram(df2, x='Recon_Ratio', nbins=50,
                       color_discrete_sequence=['#e67e22'])
    fig.add_vline(x=1, line_dash='dash', line_color='white',
                  annotation_text='Break-even')
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Avg War Cost vs Reconstruction Cost by Conflict Type")
cost_type = df2.groupby('Conflict_Type').agg(
    Avg_War_Cost=('War_Cost_B', 'mean'),
    Avg_Recon_Cost=('Recon_Cost_B', 'mean')
).reset_index()
fig = px.bar(cost_type, x='Conflict_Type',
             y=['Avg_War_Cost', 'Avg_Recon_Cost'],
             barmode='group',
             labels={'value': 'Cost ($Billion)', 'variable': 'Type'},
             color_discrete_map={'Avg_War_Cost': '#e74c3c',
                                 'Avg_Recon_Cost': '#e67e22'})
st.plotly_chart(fig, use_container_width=True)