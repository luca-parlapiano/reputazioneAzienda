from fastapi import FastAPI
from pydantic import BaseModel

from src.predict import predict_sentiment

app = FastAPI(
    title="Sentiment Analysis API",
    description="API per classificare il sentiment dei testi",
    version="1.0"
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/predict")
def predict(request: TextRequest):
    result = predict_sentiment(request.text)
    return result