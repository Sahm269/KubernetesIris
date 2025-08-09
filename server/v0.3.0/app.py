# server/v0.3.0/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.svm import SVC
import joblib
import numpy as np

# Charger modèle
model_v3 = joblib.load("model_v3.pkl")

# Définir le schéma d'entrée
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# API
app = FastAPI()

@app.post("/predict/v3")
def predict_v3(data: IrisInput):
    X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model_v3.predict(X)[0]
    return {"version": "0.3.0", "prediction": int(prediction)}

@app.get("/version")
def version():
    return {"version": "0.3.0"}
