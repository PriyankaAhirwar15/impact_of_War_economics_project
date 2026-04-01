import os
import pandas as pd
import streamlit as st

@st.cache_data # This saves memory and speeds up the app
def load_data():
    # This finds the folder where utils.py is sitting
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    # This points to the dataset inside the 'War_Economic_Project' folder
    # Note: If your CSV is in the main folder, remove 'dataset/'
    csv_path = os.path.join(base_dir, 'war_economic_impact_dataset.csv')
    
    return pd.read_csv(csv_path)