import pandas as pd
import numpy as np
import joblib
import math
loaded_model = joblib.load('model.joblib')
data = {
    "Age": 20 ,
    "Gender": "Male",
    "Occupation": "Scientist",
    "Sleep Hours": 5.8,
    "Physical Activity (hrs/week)": 2.8,
    "Caffeine Intake (mg/day)": 95,
    "Alcohol Consumption (drinks/week)": 5,
    "Smoking": "Yes",
    "Family History of Anxiety": "Yes",
    "Stress Level (1-10)": 4,
    "Heart Rate (bpm)": 100,
    "Breathing Rate (breaths/min)": 13,
    "Sweating Level (1-5)": 3,
    "Dizziness": "Yes",
    "Medication": "No",
    "Therapy Sessions (per month)": 1,
    "Recent Major Life Event": "Yes",
    "Diet Quality (1-10)": 8,
}

df = pd.DataFrame([data])


prediction = loaded_model.predict(df)   
result = round(float(prediction[0])) 

print(f"Prediction: {result}")