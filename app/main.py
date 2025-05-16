import streamlit as st
import pandas as pd
import joblib
from recommendation_engine import get_recommendations
import os

# Load the trained model (adjust path if needed)
model_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../models/best_model.joblib"))
model = joblib.load(model_path)  # Save your best model here

st.set_page_config(page_title="Healthcare Risk Predictor", layout="centered")

# App title
st.title("🩺 Personalized Healthcare Risk Prediction")

st.markdown("Fill out the form below to check your **risk of diabetes** and get **personalized health advice**.")

# Input form
with st.form("health_form"):
    HighBP = st.selectbox("Do you have high blood pressure?", ["No", "Yes"])
    HighChol = st.selectbox("Do you have high cholesterol?", ["No", "Yes"])
    BMI = st.number_input("Your BMI", min_value=10.0, max_value=60.0, step=0.1)
    Smoking = st.selectbox("Do you smoke?", ["No", "Yes"])
    PhysicalActivity = st.selectbox("Do you do regular physical activity?", ["Yes", "No"])
    Fruits = st.selectbox("Do you eat fruits regularly?", ["Yes", "No"])

    submitted = st.form_submit_button("Check My Risk")

# Process input & predict
if submitted:
    user_data = {
    "HighBP": 1 if HighBP == "Yes" else 0,
    "HighChol": 1 if HighChol == "Yes" else 0,
    "CholCheck": 1,  # default or add input
    "BMI": BMI,
    "Smoker": 1 if Smoking == "Yes" else 0,
    "Stroke": 0,
    "HeartDiseaseorAttack": 0,
    "PhysActivity": 1 if PhysicalActivity == "Yes" else 0,
    "Fruits": 1 if Fruits == "Yes" else 0,
    "Veggies": 1,  # assume healthy
    "HvyAlcoholConsump": 0,
    "AnyHealthcare": 1,
    "NoDocbcCost": 0,
    "GenHlth": 3,  # neutral rating
    "MentHlth": 0,
    "PhysHlth": 0,
    "DiffWalk": 0,
    "Sex": 1,  # assume male, or add gender input
    "Age": 9,  # assume a default group, or add input
    "Education": 4,
    "Income": 5
}

    # Convert to DataFrame for model
    input_df = pd.DataFrame([user_data])

    # Predict
    prediction = model.predict(input_df)[0]

    # Display result
    if prediction == 1:
        st.error("⚠️ You are at high risk for diabetes.")
    else:
        st.success("✅ You are currently at low risk for diabetes.")

    # Show recommendations
    recs = get_recommendations(user_data, prediction)
    st.subheader("Personalized Recommendations")
    for rec in recs:
        st.markdown(f"- {rec}")
