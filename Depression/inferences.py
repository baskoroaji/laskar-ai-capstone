import pandas as pd
import numpy as np
import joblib
loaded_model = joblib.load('model.joblib')
data = {
    "Gender": "Male",
    "Age": 20 ,
    "Profession": "Student",
    "Academic Pressure": 5.0,
    "Work Pressure": 0.0,
    "Study Satisfaction": 1.0,
    "Job Satisfaction": 0.0,
    "Sleep Duration": "'7-8 hours'",
    "Dietary Habits": "Healthy",
    "Degree": "BA",
    "Have you ever had suicidal thoughts ?": "Yes",
    "Work/Study Hours": 5.0,
    "Financial Stress": 5.0,
    "Family History of Mental Illness": "Yes"
}

df = pd.DataFrame([data])


proba = loaded_model.predict_proba(df)[0] 
prediction = loaded_model.predict(df)[0]      

label = "Yes" if prediction == 1 else "No"
confidence = proba[prediction]                

print(f"Prediction: {label} (Confidence: {confidence * 100:.2f}%)")