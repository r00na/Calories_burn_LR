import streamlit as st
import numpy as np
import joblib

model = joblib.load('linear_regressor_model.pkl')

st.set_page_config(page_title="🔥 Calories Burn Predictor", page_icon="🔥", layout="centered")

st.markdown(
    """
    <style>
        body { background-color: #D5F5E3; }
        .stButton > button { background-color: #27AE60; color: white; font-size: 18px; padding: 10px; border-radius: 10px; }
        .stButton > button:hover { background-color: #1E8449; }
        .stSlider .st-bm { color: #2ECC71 !important; }
    </style>
    """, unsafe_allow_html=True
)



st.markdown("""
    <h1 style='text-align: center; color: #2ECC71;'>🔥 Calories Burn Predictor 🔥</h1>
    <p style='text-align: center; color: #555;'>Enter your workout details to estimate calories burned.</p>
    """, unsafe_allow_html=True)

st.markdown("---")


gender = st.radio(" Select Gender:", ["Male", "Female"], horizontal=True)
age = st.slider(" Age:", 10, 100, 25)
height = st.slider(" Height (cm):", 100, 220, 170)
weight = st.slider(" Weight (kg):", 30, 200, 70)
duration = st.slider(" Workout Duration (minutes):", 1, 120, 30)
heart_rate = st.slider(" Heart Rate (bpm):", 50, 200, 100)

gender_numeric = 1 if gender == "Male" else 0

user_input = np.array([[gender_numeric, age, height, weight, duration, heart_rate]])   

st.markdown("---")

if st.button("Predict Calories Burned"):
    prediction = model.predict(user_input)[0]
    st.success(f"🔥 Estimated Calories Burned: {prediction:.2f} kcal")
    st.balloons()

st.markdown("---")
