# Heart Disease Prediction Model

This project implements a machine learning model to predict heart disease using patient health data. It includes both the model training code and a Flask API for making predictions.

## Project Structure
├── data/  
│ └── input/  
│ └── heart.csv # Dataset with patient health information  
├── models/  
│ └── RandomForestClassifier/  
│ └── best_heart_disease_model.pkl  
├── src/  
│ └── heart_model_api.py # Flask API implementation  
├── .gitignore  
└── requirements.txt

## Dataset Description

The dataset (`heart.csv`) contains various health metrics and a target variable indicating the presence of heart disease. Key features include:

- age: Age of the patient
- sex: Gender (1 = male, 0 = female)
- cp: Chest pain type
- trestbps: Resting blood pressure
- chol: Serum cholesterol
- fbs: Fasting blood sugar
- restecg: Resting electrocardiographic results
- thalach: Maximum heart rate achieved
- exang: Exercise induced angina
- oldpeak: ST depression induced by exercise
- slope: Slope of the peak exercise ST segment
- ca: Number of major vessels colored by fluoroscopy
- thal: Thalassemia type
- target: Heart disease presence (1 = present, 0 = absent)

## API Usage

The Flask API provides a simple endpoint for making predictions:
python
POST /predict
Example request body:
{
"age": 52,
"sex": 1,
"cp": 0,
"trestbps": 125,
"chol": 212,
"fbs": 0,
"restecg": 1,
"thalach": 168,
"exang": 0,
"oldpeak": 1.0,
"slope": 2,
"ca": 2,
"thal": 3
}
Response:
{
"prediction": 0 # 0 = No heart disease, 1 = Heart disease present
}