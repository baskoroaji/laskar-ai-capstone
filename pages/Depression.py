import streamlit as st
import time
import numpy as np
import pandas as pd
import joblib
import os
from datetime import datetime
st.set_page_config(page_title="Depression Prediction")

st.markdown("# Depression Prediction")
st.sidebar.header("Depression Prediction")

base_path = os.path.dirname(__file__)  # Current file's dir (i.e., 'pages/')
model_path = os.path.abspath(os.path.join(base_path, "..", "Depression", "model.joblib"))

depression_model = joblib.load(model_path)

degree_map = {
    "Class 12": "'Class 12'", 
    "Bachelor of Architecture": 'B.Arch', 
    "Bachelor of Commerce": 'B.Com', 
    "Bachelor of Education": 'B.Ed', 
    "Bachelor of Computer Application": 'BCA', 
    "Bachelor of Technology": 'B.Tech', 
    "Master of Science": 'MSc', 
    "Master of Computer Application": 'MCA', 
    "Bachelor of Science": 'BSc', 
    "Bachelor of Hotel Management": 'BHM', 
    "Bachelor of Pharmacy": 'B.Pharm', 
    "Bachelor of Business Administration": 'BBA', 
    "Master of Technology": 'M.Tech', 
    "Master of Commerce": 'M.Com', 
    "Bachelor of Arts": 'BA', 
    "Bachelor of Medicine and Surgery": 'MBBS', 
    "Master of Arts": 'MA', 
    "Master of Business Administration": 'MBA',
    "Bachelor of Engineering": 'BE', 
    "Doctor of Philosophy": 'PhD', 
    "Master of Education": 'M.Ed', 
    "Master of Pharmacy": 'M.Pharm', 
    "Bachelor of Law": 'LLB' , 
    "Doctor of Medicine": 'MD',
    "Law": 'LLM', 
    "Master of Hotel Management": 'MHM', 
    "Master of Engineering": 'ME', 
    'Others': "Others"
}

st.header(f"Enter Demographic Information for Prediction")
birth_year = st.number_input("Enter your birth year:", min_value=1997, max_value=2012, value=2000)
current_year = datetime.now().year
age = current_year - birth_year
isGenZ = 1997 <= birth_year <= 2012
st.write(f" Age: **{age}**")
gender = st.selectbox("Gender", ["Male", "Female"])
profession = st.selectbox("Profession", ["Student"])   
study_satisfaction = st.radio("Study Satisfaction",options=[0,1,2,3,4,5,6,7,8,9,10], horizontal=True)
work_study_hours = st.slider("Work/Study Hours per day", 0, 12, 6)
academic_pressure = st.radio("academic pressure",options=[0,1,2,3,4,5], horizontal=True)
job_satisfaction = st.radio("job satisfaction",options=[0], horizontal=True)
work_pressure = st.radio("work pressure",options=[0], horizontal=True)
Degree = st.selectbox("Degree", list(degree_map.keys()))
thoughts = st.selectbox("Have you ever had suicidal thoughts ?", ["Yes", "No"])
diet = st.selectbox("Dietary Habits", ["Healthy","Moderate","Unhealthy", "Others"])
financial = st.radio("Financial Stress",options=[0,1,2,3,4,5], horizontal=True)
sleep = st.selectbox("Sleep Duration", ["5-6 hours", "Less than 5 hours","7-8 hours", "More than 8 hours", "Others"])
family = st.selectbox("Family History of Mental Illness", ["Yes", "No"])

pred_data = {
    "Gender": gender,
    "Age": age ,
    "Profession": profession,
    "Academic Pressure": academic_pressure,
    "Work Pressure": work_pressure,
    "Study Satisfaction": study_satisfaction,
    "Job Satisfaction": job_satisfaction,
    "Sleep Duration": sleep,
    "Dietary Habits": diet,
    "Degree": Degree,
    "Have you ever had suicidal thoughts ?": thoughts,
    "Work/Study Hours": work_study_hours,
    "Financial Stress": financial,
    "Family History of Mental Illness": family
}

input_data = pd.DataFrame([pred_data])
if st.button("Predict"):
    prediction = depression_model.predict(input_data)[0]
    prediction_proba = depression_model.predict_proba(input_data)[0]
    confidence = prediction_proba[prediction] 

    label = "Yes" if prediction == 1 else "No"
    st.subheader(f"🧾 Depression Prediction: **{label}**")
    st.write(f"🧠 Confidence: **{confidence*100:.2f}%**")