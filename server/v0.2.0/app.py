# server/v0.2.0/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from sklearn.linear_model import LogisticRegression
import joblib
import numpy as np

# Charger modèle
model_v2 = joblib.load("model_v2.pkl")

# Définir le schéma d'entrée
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

# API
app = FastAPI()

@app.post("/predict/v2")
def predict_v2(data: IrisInput):
    X = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model_v2.predict(X)[0]
    return {"version": "0.2.0", "prediction": int(prediction)}

@app.get("/version")
def version():
    return {"version": "0.2.0"}
