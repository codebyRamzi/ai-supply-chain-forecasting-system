from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("models/random_forest_model.pkl")

# Create FastAPI app
app = FastAPI()

# Input schema
class SalesInput(BaseModel):
    Store: int
    Dept: int
    IsHoliday: int
    Year: int
    Month: int
    Week: int

# Root route
@app.get("/")
def home():
    return {"message": "AI Forecasting API is running"}

# Prediction route
@app.post("/predict")
def predict_sales(data: SalesInput):

    input_data = pd.DataFrame({
        "Store": [data.Store],
        "Dept": [data.Dept],
        "IsHoliday": [data.IsHoliday],
        "Year": [data.Year],
        "Month": [data.Month],
        "Week": [data.Week]
    })

    prediction = model.predict(input_data)

    return {
        "predicted_sales": float(prediction[0])
    }