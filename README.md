❤️ Heart Disease Prediction System

A Machine Learning–based web application that predicts the likelihood of heart disease using patient medical parameters. The system uses a trained classification model and provides predictions through a FastAPI backend and an interactive Streamlit frontend.

📌 Project Overview

Early detection of heart disease can save lives. This project applies machine learning techniques to analyze patient health data and predict whether a person is at risk of heart disease.

The application consists of:

A trained ML classification model

A FastAPI backend exposing a REST API

A Streamlit-based frontend for user interaction

⚙️ Features

User-friendly web interface

Accepts clinical input parameters

Real-time prediction results

Scikit-learn based model

REST API support

🧠 Machine Learning Model

Algorithm: Logistic Regression

Framework: scikit-learn

Data Preprocessing:

Feature scaling

Train-test split

Output:

0 → Low Risk

1 → High Risk

🧾 Input Parameters

Age

Sex

Chest Pain Type (cp)

Resting Blood Pressure (trestbps)

Cholesterol (chol)

Fasting Blood Sugar (fbs)

Rest ECG (restecg)

Maximum Heart Rate (thalach)

Exercise Induced Angina (exang)

Oldpeak

ST Slope (slope)

Number of Major Vessels (ca)

Thalassemia (thal)

🏗️ Project Structure
heart_disease_project/
│
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   └── model/
│       └── heart_model.pkl
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── model_training/
│   └── train_model.ipynb
│
└── README.md

▶️ How to Run Locally
Backend
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn app:app --reload

Frontend
cd frontend
pip install -r requirements.txt
streamlit run app.py

📊 Output Interpretation

Low Risk: Patient unlikely to have heart disease

High Risk: Patient may have heart disease and should seek medical consultation

🛠️ Technologies Used

Python

scikit-learn

Pandas

FastAPI

Streamlit

Joblib

📌 Future Enhancements

Add more ML algorithms

Improve UI/UX

Add authentication

Store prediction history

Add explainability (SHAP / feature importance)

👤 Author

Faiz Ahmed Khan
