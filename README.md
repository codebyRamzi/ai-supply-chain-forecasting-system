# AI Supply Chain Forecasting System

An end-to-end AI-powered demand forecasting system built using Machine Learning, FastAPI, and Streamlit.

This project predicts future weekly sales using historical retail data and provides real-time forecasting through a production-style API architecture.

---

# Features

- Machine Learning-based sales forecasting
- Interactive Streamlit dashboard
- Real-time prediction API using FastAPI
- Forecast visualization charts
- AI-generated business insights
- KPI metrics dashboard
- Production-style frontend/backend architecture

---

# Tech Stack

## Programming Language
- Python

## Machine Learning
- Scikit-learn
- Random Forest Regressor
- XGBoost

## Data Processing
- Pandas
- NumPy

## Visualization
- Matplotlib

## Frontend
- Streamlit

## Backend API
- FastAPI
- Uvicorn

---

# Project Architecture

```text
Streamlit Frontend
        ↓
FastAPI Backend
        ↓
Machine Learning Model
        ↓
Sales Forecast Predictions
```

---

# Folder Structure

```text
AI-Supply-Chain-Forecasting-System/
│
├── api/
│   └── main.py
│
├── app/
│   └── app.py
│
├── data/
│   ├── train.csv
│   ├── stores.csv
│   ├── features.csv
│   └── test.csv
│
├── models/
│
├── notebooks/
│   └── eda.ipynb
│
├── screenshots/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# Dataset

This project uses the Walmart Sales Forecasting Dataset from Kaggle.

Dataset includes:
- Store information
- Department data
- Weekly sales
- Holiday indicators
- Retail forecasting patterns

---

# Installation Guide

## 1. Clone Repository

```bash
git clone <your-github-repository-link>
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Model File

The trained model file is not included in this repository due to file size limitations.

To regenerate the model:

1. Open:
   `notebooks/eda.ipynb`

2. Run all notebook cells

3. The trained model will automatically be saved inside:

```text
models/random_forest_model.pkl
```

---

# Run FastAPI Backend

Start backend server:

```bash
uvicorn api.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# API Documentation

Interactive Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

---

# Run Streamlit Frontend

Start frontend dashboard:

```bash
streamlit run app/app.py
```

---

# Machine Learning Workflow

1. Data preprocessing
2. Feature engineering
3. Model training
4. Model evaluation
5. Forecast prediction
6. API deployment
7. Frontend integration

---

# Forecasting Features

The model predicts weekly sales using:
- Store number
- Department number
- Holiday information
- Month
- Year
- Week information

---

# Future Improvements

- LSTM-based deep learning forecasting
- Transformer models
- SHAP explainability
- Cloud deployment
- Authentication system
- Database integration
- Real-time streaming predictions
- Advanced forecasting analytics

---


# Learning Outcomes

This project demonstrates:
- Machine Learning
- Time-series forecasting
- API development
- Frontend/backend integration
- AI deployment concepts
- Production AI architecture

---

# Author

Ramzi

AI & Python Internship Project
