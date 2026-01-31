import streamlit as st
import pandas as pd
import joblib

import joblib

model = joblib.load("models/aqi_model.pkl") 
le = joblib.load("aqi_label_encoder.pkl")

st.title("Pakistan AQI Forecast")
city = st.selectbox("Select City", ["Islamabad"])

st.write("Next 3 days AQI forecast:")
forecast_df = pd.read_csv("aqi_forecast_next3days.csv")
st.table(forecast_df)
