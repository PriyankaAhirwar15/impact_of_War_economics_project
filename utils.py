import os
import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    base = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(base, 'war_economic_impact_dataset.csv')
    return pd.read_csv(path)