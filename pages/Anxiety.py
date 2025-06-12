import streamlit as st
import time
import numpy as np
import pandas as pd
import joblib
import os
from datetime import datetime
st.set_page_config(page_title="Anxiety Level Prediction")

st.markdown("# Anxiety Level Prediction")
st.sidebar.header("Anxiety Level Prediction")

base_path = os.path.dirname(__file__)
model_path = os.path.abspath(os.path.join(base_path, "..", "Anxiety", "model.joblib"))

anxiety_model = joblib.load(model_path)

occupation_map = {
   'Freelancer': 'Freelancer',
   'Chef': 'Chef',
   'Artist': 'Artist',
   'Student': 'Student',
   'Nurse': 'Nurse',
   'Other': 'Other',
   'Musician': 'Musician',
   'Engineer': 'Engineer',
   'Doctor': 'Doctor',
   'Athlete': 'Athlete',
   'Scientist': 'Scientist',
   'Teacher': 'Teacher',
   'Lawyer': 'Lawyer'
}

st.header(f"Enter Demographic Information for Prediction")
birth_year = st.number_input("Enter your birth year:", min_value=1997, max_value=2012, value=2000)
current_year = datetime.now().year
age = current_year - birth_year
isGenZ = 1997 <= birth_year <= 2012
st.write(f" Age: **{age}**")
gender = st.selectbox("Gender", ["Male", "Female", "Others"])
Occupation = st.selectbox("Degree", list(occupation_map.keys())) 
Sleep_Hours = st.number_input("Enter your Sleep Hours:", min_value=0, max_value=500, value=50)
Physical_Activity = st.number_input("Enter your Physical Activity (hrs/week):", min_value=0, max_value=500, value=50)
Caffeine_Intake = st.number_input("Enter your Caffeine Intake (mg/day):", min_value=0, max_value=500, value=50)
Alcohol_Consumption = st.number_input("Enter your Alcohol Consumption (drinks/week):", min_value=0, max_value=500, value=50)
Smoking = st.selectbox("Are you Smoking ?", ["Yes", "No"])
Family_History_of_Anxiety  = st.selectbox("Do You Have a Family History of Anxiety ?", ["Yes", "No"])
Stress = st.radio("Stress Level (1-10)",options=[0,1,2,3,4,5,6,7,8,9,10], horizontal=True)
Heart_Rate = st.number_input("Enter your Heart Rate:", min_value=0, max_value=500, value=50)
Breathing_Rate = st.number_input("Enter your Breathing Rate", min_value=0, max_value=500, value=50)
Sweating_Level = st.radio("Are you sweating a lot?",options=[0,1,2,3,4,5], horizontal=True)
Dizziness = st.selectbox("Have you ever had dizziness ?", ["Yes", "No"])
Medication = st.selectbox("have you ever taken medication ?", ["Yes", "No"])
Therapy_Sessions = st.number_input("Enter your Therapy Sessions per Months:", min_value=0, max_value=500, value=50)
Major_Life_Event  = st.selectbox("is there a recent major life event ?", ["Yes", "No"])
Diet_Quality = st.radio("Diet Quality",options=[0,1,2,3,4,5,6,7,8,9,10], horizontal=True)

pred_data = {
    "Age": age ,
    "Gender": gender,
    "Occupation": Occupation,
    "Sleep Hours": Sleep_Hours,
    "Physical Activity (hrs/week)": Physical_Activity,
    "Caffeine Intake (mg/day)": Caffeine_Intake,
    "Alcohol Consumption (drinks/week)": Alcohol_Consumption,
    "Smoking": Smoking,
    "Family History of Anxiety": Family_History_of_Anxiety,
    "Stress Level (1-10)": Stress,
    "Heart Rate (bpm)": Heart_Rate,
    "Breathing Rate (breaths/min)": Breathing_Rate,
    "Sweating Level (1-5)": Sweating_Level,
    "Dizziness": Dizziness,
    "Medication": Medication,
    "Therapy Sessions (per month)": Therapy_Sessions,
    "Recent Major Life Event": Major_Life_Event,
    "Diet Quality (1-10)": Diet_Quality,
}

input_data = pd.DataFrame([pred_data])
if st.button("Predict"):
    prediction = anxiety_model.predict(input_data)   
    result = round(float(prediction[0])) 

    st.subheader(f"🧾 Anxiety Level Prediction: **{result}**")