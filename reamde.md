AQI Forecast Hackathon App
Project Overview

This project predicts the Air Quality Index (AQI) category for the next 3 days using machine learning models (RandomForest and XGBoost) based on historical pollution data.

The project includes:

Data preprocessing and feature engineering

RandomForest and XGBoost model training

Forecasting AQI categories for the next 3 days

Saving/loading models and LabelEncoder

Exporting forecast to CSV

Folder Structure
model/
│   hackathon_app.py
│   aqi_model.pkl
│   aqi_label_encoder.pkl
│   aqi_forecast_next3days.csv
│   README.md
└───data/
     └───Training/
         concatenated_dataset_Aug_2021_to_July_2024.csv

How to Run

Install dependencies (Python 3.13+ recommended):

pip install pandas scikit-learn xgboost matplotlib joblib


Run the app:

python hackathon_app.py


The script will:

Train the model (if needed)

Generate a 3-day AQI forecast

Save the forecast as aqi_forecast_next3days.csv

Save the model as aqi_model.pkl and label encoder as aqi_label_encoder.pkl

Visualize Forecast:
A plot of predicted AQI categories for the next 3 days will be displayed automatically.

Notes

Ensure all files (hackathon_app.py, aqi_model.pkl, aqi_label_encoder.pkl, aqi_forecast_next3days.csv) are in the same folder.

The dataset (concatenated_dataset_Aug_2021_to_July_2024.csv) should be inside data/Training/.

The code uses LabelEncoder to encode AQI categories (Good, Moderate, Unhealthy, Very Unhealthy, Hazardous).

Author

Kiran Hamza
Hackathon Participant