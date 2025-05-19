import streamlit as st

# Page config
st.set_page_config(
    page_title="Calories Burn Predictor",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS Styling 
st.markdown("""
<style>
html, body, [data-testid="stApp"] {
    background: linear-gradient(to bottom right, #e8f0fe, #d0dbed);
    font-family: 'Segoe UI', sans-serif;
}

.title {
    background-color: #1e3a5f;
    color: white;
    padding: 25px;
    border-radius: 16px;
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    margin-bottom: 0px;
    box-shadow: 0 8px 16px rgba(0,0,0,0.1);
}

.main-box {
    background-color: #ffffff;
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-top: 0px;
    border: 1px solid #e6edf7;
}

.section-header {
    color: #1e3a5f;
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 15px;
    border-bottom: 2px solid #d0dbed;
    padding-bottom: 8px;
}

.stButton > button {
    background-color: #1e3a5f !important;
    color: white !important;
    border: none !important;
    padding: 14px 35px !important;
    font-size: 16px !important;
    border-radius: 10px !important;
    transition: 0.3s ease !important;
    font-weight: 600 !important;
    letter-spacing: 0.5px !important;
    margin: auto;
    display: block;
}

.stButton > button:hover {
    background-color: #163250 !important;
}

input:focus, select:focus, textarea:focus {
    border-color: #1e3a5f !important;
    box-shadow: 0 0 0 0.15rem rgba(30, 58, 95, 0.25) !important;
}

.result-box {
    background-color: #f7faff;
    border-left: 5px solid #4a6fa5;
    padding: 30px;
    border-radius: 12px;
    margin-top: 35px;
    text-align: center;
}

.footer {
    background-color: #1e3a5f;
    color: #ffffff;
    text-align: center;
    padding: 20px;
    border-radius: 12px;
    font-size: 14px;
    margin-top: 60px;
}

.metric-container {
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
}

.metric-box {
    background-color: #f7faff;
    padding: 15px;
    border-radius: 10px;
    text-align: center;
    flex: 1;
    margin: 0 5px;
    border: 1px solid #e6edf7;
}

.metric-value {
    font-size: 24px;
    font-weight: bold;
    color: #1e3a5f;
}

.metric-label {
    font-size: 14px;
    color: #4a6fa5;
    margin-top: 5px;
}
</style>
""", unsafe_allow_html=True)

# ==== HEADER ====
st.markdown("<div class='title'>Calories Burn Prediction</div>", unsafe_allow_html=True)

# ==== FORM ====
st.markdown("<div class='main-box'>", unsafe_allow_html=True)

with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        age = st.number_input("Age", 10, 100, 25)
        height = st.number_input("Height (cm)", 100, 220, 170)

    with col2:
        weight = st.number_input("Weight (kg)", 30, 200, 70)
        duration = st.number_input("Workout Duration (minutes)", 1, 120, 30)
        heart_rate = st.number_input("Heart Rate (bpm)", 50, 200, 100)

    st.markdown("---")
    col3, col4 = st.columns(2)

    with col3:
        workout_type = st.selectbox("Workout Type", [
            "Running", "Walking", "Cycling", "Swimming",
            "Weight Training", "HIIT", "Yoga", "Other"
        ])

    with col4:
        intensity = st.selectbox(
            "Workout Intensity",
            options=["Low", "Moderate", "High", "Very High"]
        )

    submit = st.form_submit_button("Calculate Calories Burned")

st.markdown("</div>", unsafe_allow_html=True)

# ==== PREDICTION ====
if submit:
    gender_factor = 1.0 if gender == "Male" else 0.85
    intensity_factor = {"Low": 0.6, "Moderate": 0.8, "High": 1.0, "Very High": 1.2}[intensity]
    workout_factor = {
        "Running": 1.2, "Walking": 0.7, "Cycling": 1.0,
        "Swimming": 1.3, "Weight Training": 0.9,
        "HIIT": 1.4, "Yoga": 0.6, "Other": 1.0
    }[workout_type]

    base_calories = (duration * heart_rate * 0.1)
    weight_factor = weight / 70
    age_factor = 1 - ((age - 25) * 0.005) if age > 25 else 1 + ((25 - age) * 0.003)

    prediction = base_calories * gender_factor * intensity_factor * workout_factor * weight_factor * age_factor

    kcal_per_min = prediction / duration
    efficiency = intensity_factor * workout_factor * 100
    met_value = (prediction / (weight * duration)) * 200

    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.subheader("Estimated Calories Burned")
    st.markdown(f"### 🔥 {int(prediction)} kcal")

    col1, col2, col3 = st.columns(3)
    col1.metric("kcal/min", f"{kcal_per_min:.1f}")
    col2.metric("Efficiency", f"{efficiency:.0f}%")
    col3.metric("MET", f"{met_value:.1f}")
    st.markdown("</div>", unsafe_allow_html=True)

    tip = (
        "Consider increasing your workout intensity or duration for better calorie burn."
        if prediction < 200 else
        "You're in a good calorie-burning zone. Try incorporating interval training."
        if prediction < 400 else
        "Excellent calorie burn! Stay hydrated and allow recovery time."
    )
    st.info(f"💡 **Professional Fitness Insight:** {tip}")

# ==== FOOTER ====
st.markdown("""
    <div class='footer'>
        <div style='font-weight: bold; margin-bottom: 8px; font-size: 16px;'>HealthTrack Pro</div>
        <div>Smart Tools for Smarter Fitness Goals</div>
        <div style='margin-top: 12px; font-size: 12px;'>© 2025 – Developed with 💙 for a healthier you</div>
    </div>
""", unsafe_allow_html=True)

