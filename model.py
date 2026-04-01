import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error

def train_model(df):
    df = df.copy()

    features = ['Conflict_Type', 'Region', 'GDP_Change_%',
                'Inflation_Rate_%', 'Unemployment_Spike_Percentage_Points']
    target = 'Estimated_Reconstruction_Cost_USD'

    df = df[features + [target]].dropna()

    le_type = LabelEncoder()
    le_region = LabelEncoder()
    df['Conflict_Type'] = le_type.fit_transform(df['Conflict_Type'])
    df['Region'] = le_region.fit_transform(df['Region'])

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    mae = mean_absolute_error(y_test, model.predict(X_test))
    return model, le_type, le_region, mae

def predict_cost(model, le_type, le_region,
                 conflict_type, region, gdp_change, inflation, unemp_spike):
    type_enc = le_type.transform([conflict_type])[0]
    region_enc = le_region.transform([region])[0]
    X = np.array([[type_enc, region_enc, gdp_change, inflation, unemp_spike]])
    return model.predict(X)[0]