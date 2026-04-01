import streamlit as st
import pandas as pd
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils import load_data

st.set_page_config(page_title="KPI Dashboard", layout="wide", page_icon="📊")
st.title("📊 KPI Dashboard — Human Cost of War at a Glance")
st.markdown("Aggregate headline numbers across all 100,000 conflict records.")

df = load_data()

st.divider()
c1, c2, c3, c4 = st.columns(4)
c1.metric("Total Records",      f"{len(df):,}")
c2.metric("Unique Conflicts",   f"{df['Conflict_Name'].nunique():,}")
c3.metric("Countries Affected", f"{df['Primary_Country'].nunique():,}")
c4.metric("Regions Covered",    f"{df['Region'].nunique():,}")

st.divider()
c5, c6, c7, c8 = st.columns(4)
c5.metric("Avg GDP Change",      f"{df['GDP_Change_%'].mean():.1f}%")
c6.metric("Avg Inflation Rate",  f"{df['Inflation_Rate_%'].mean():.1f}%")
c7.metric("Avg Extreme Poverty", f"{df['Extreme_Poverty_Rate_%'].mean():.1f}%")
c8.metric("Avg Food Insecurity", f"{df['Food_Insecurity_Rate_%'].mean():.1f}%")

st.divider()
c9, c10, c11, c12 = st.columns(4)
c9.metric("Avg Unemployment Spike", f"{df['Unemployment_Spike_Percentage_Points'].mean():.1f}pp")
c10.metric("Avg Currency Deval.",   f"{df['Currency_Devaluation_%'].mean():.1f}%")
c11.metric("Total War Cost",        f"${df['Cost_of_War_USD'].sum()/1e12:.1f} Trillion")
c12.metric("Total Reconstruction",  f"${df['Estimated_Reconstruction_Cost_USD'].sum()/1e12:.1f} Trillion")

st.divider()
st.subheader("📋 Raw Data Sample")
st.dataframe(df.sample(20), use_container_width=True)