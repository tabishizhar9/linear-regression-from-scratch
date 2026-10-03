import json
from fastapi import FastAPI
from pathlib import Path

MODEL_PATH = Path(__file__).parent.parent / "model" / "model.json"


with open(MODEL_PATH, "r")as f:
    params = json.load(f)

w = params["w"]
b = params["b"]

app = FastAPI()


@app.get("/predict")
def predict(income: float):
    prediction = w * income + b
    return {"predicted_value": prediction}