import os
import requests
from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}


app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI backend running 🎉"}

@app.get("/ping")
def ping():
    return {"status": "ok"}

@app.post("/predict")
def predict(prompt: str):
    data = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=data)
    

     # Debugging helper: check status first
    if response.status_code != 200:
        return {
            "error": f"Request failed with status {response.status_code}",
            "details": response.text
        }

    try:
        return response.json()
    except Exception as e:
        return {"error": "Failed to parse JSON", "raw": response.text, "exception": str(e)}