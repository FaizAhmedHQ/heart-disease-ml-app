from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI()

# Load model and scaler
model = joblib.load("model/heart_model.pkl")
scaler = joblib.load("model/scaler.pkl")

# Input schema
class PatientData(BaseModel):
    Age: float
    Sex: int
    Chest_Pain_Type: int
    Resting_Blood_Pressure: float
    Cholesterol: float
    Fasting_Blood_Sugar: int
    Resting_ECG: int
    Max_Heart_Rate: float
    Exercise_Induced_Angina: int
    ST_Depression: float
    ST_Slope: int
    Num_Major_Vessels: int
    Thalassemia: int


@app.get("/")
def home():
    return {"message": "Heart Disease Prediction API Running"}


@app.post("/predict")
def predict(data: PatientData):

    input_data = np.array([[

        data.Age,
        data.Sex,
        data.Chest_Pain_Type,
        data.Resting_Blood_Pressure,
        data.Cholesterol,
        data.Fasting_Blood_Sugar,
        data.Resting_ECG,
        data.Max_Heart_Rate,
        data.Exercise_Induced_Angina,
        data.ST_Depression,
        data.ST_Slope,
        data.Num_Major_Vessels,
        data.Thalassemia

    ]])

    scaled_data = scaler.transform(input_data)
    prediction = model.predict(scaled_data)[0]

    result = "Heart Disease Detected" if prediction == 1 else "No Heart Disease"

    return {
        "prediction": int(prediction),
        "result": result
    }
