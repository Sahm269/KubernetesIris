# server/app.py
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
import joblib
import numpy as np
from sklearn.datasets import load_iris

# Charger modèle
model_v1 = joblib.load("model_v1.pkl")


# Définir le schéma d'entrée
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# API
app = FastAPI()


@app.post("/predict/v1")
def predict_v1(data: IrisInput):
    X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model_v1.predict(X)[0]
    return {"version": "0.1.0", "prediction": int(prediction)}


@app.get("/version")
def version():
    return {"version": "0.1.0"}  