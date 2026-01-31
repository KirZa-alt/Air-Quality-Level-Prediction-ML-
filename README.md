AQI Forecast App 🌿

Predict Air Quality Index (AQI) for the next 3 days using machine learning. Built with Python, XGBoost, RandomForest, and Streamlit for an interactive interface.

Features 🚀

Predicts AQI categories: Good, Moderate, Unhealthy, Very Unhealthy

Uses historical PM2.5 and AQI data for accurate forecasting

Generates visual forecast plots

Streamlit interface for easy interaction

Folder Structure 📂
model/
├─ hackathon_app.py        # Main ML code
├─ aqi_model.pkl           # Trained XGBoost model
├─ aqi_label_encoder.pkl   # Label encoder for AQI categories
├─ aqi_forecast_next3days.csv  # Forecast results
└─ data/
   └─ Training/
      └─ concatenated_dataset_Aug_2021_to_July_2024.csv

How to Run 💻

Clone the repo:

git clone <repo-link>
cd model


Install dependencies:

pip install pandas scikit-learn xgboost matplotlib joblib streamlit


Run Streamlit app:

streamlit run hackathon_app.py


View AQI forecast in your browser! 🌐

License ⚡

Open-source and free to use.
