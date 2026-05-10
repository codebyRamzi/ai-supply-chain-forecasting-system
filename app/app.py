import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

# Page configuration
st.set_page_config(
    page_title="AI Supply Chain Copilot",
    layout="wide"
)

# Main title
st.title("AI Supply Chain Forecasting Copilot")

st.success(
    "AI-powered demand forecasting system is active."
)

st.write(
    "Predict future weekly sales using Machine Learning + FastAPI."
)

# Sidebar
st.sidebar.header("Forecast Settings")

st.sidebar.write(
    "Adjust inputs to predict future demand."
)

# User inputs
store = st.sidebar.number_input(
    "Store Number",
    min_value=1,
    max_value=45,
    value=1
)

dept = st.sidebar.number_input(
    "Department Number",
    min_value=1,
    max_value=100,
    value=1
)

month = st.sidebar.slider(
    "Select Month",
    min_value=1,
    max_value=12,
    value=1
)

holiday = st.sidebar.selectbox(
    "Is it a Holiday Week?",
    [0, 1]
)

# Prediction button
if st.sidebar.button("Predict Sales"):

    # Send request to FastAPI backend
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        json={
            "Store": int(store),
            "Dept": int(dept),
            "IsHoliday": int(holiday),
            "Year": 2012,
            "Month": int(month),
            "Week": 1
        }
    )

    # Get prediction from API response
    prediction = response.json()["predicted_sales"]

    # Display prediction
    st.subheader("Sales Forecast Result")

    st.success(
        f"Predicted Weekly Sales: ${prediction:,.2f}"
    )

    # Forecast visualization
    future_weeks = [1, 2, 3, 4]

    future_sales = [
        prediction * 0.95,
        prediction,
        prediction * 1.05,
        prediction * 1.08
    ]

    # KPI Metrics
    col1, col2 = st.columns(2)

    col1.metric(
        "Predicted Sales",
        f"${prediction:,.0f}"
    )

    growth = (
        (future_sales[-1] - future_sales[0])
        / future_sales[0]
    ) * 100

    col2.metric(
        "Forecast Growth",
        f"{growth:.2f}%"
    )

    # Forecast chart
    fig, ax = plt.subplots(figsize=(10,5))

    ax.plot(
        future_weeks,
        future_sales,
        marker="o"
    )

    ax.set_title("4-Week Sales Forecast")
    ax.set_xlabel("Future Weeks")
    ax.set_ylabel("Predicted Sales")

    st.pyplot(fig)

    # AI-generated business insights
    st.subheader("AI Business Insights")

    if holiday == 1:
        st.info(
            "Holiday season may increase customer demand."
        )

    if month in [11, 12]:
        st.info(
            "Year-end seasonal trends often boost sales."
        )

    if dept > 50:
        st.info(
            "This department may experience specialized demand patterns."
        )

    if prediction > 20000:
        st.info(
            "High forecasted demand detected. Inventory planning is recommended."
        )

    if prediction < 5000:
        st.warning(
            "Lower expected demand detected. Overstock risk should be monitored."
        )

    # Input summary
    st.subheader("Input Summary")

    st.write(f"Store Number: {store}")
    st.write(f"Department Number: {dept}")
    st.write(f"Month: {month}")
    st.write(f"Holiday Week: {holiday}")