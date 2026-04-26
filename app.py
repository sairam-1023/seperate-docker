from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class InputData(BaseModel):
    sqft_living: float
    bedrooms: int
    bathrooms: float

app = FastAPI()

# Allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Input schema
class InputData(BaseModel):
    area: float
    bedrooms: int

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def home():
    return {"message": "Backend running"}

@app.post("/predict")
def predict(data: InputData):
    input_data = [[data.sqft_living, data.bedrooms, data.bathrooms]]
    prediction = model.predict(input_data)[0]
    return {"predicted_price": float(prediction)}