""" from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "sentiment-analysis",
            model=MODEL_NAME,
            tokenizer=MODEL_NAME
        )
    return _classifier

def predict_sentiment(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    
    if not text.strip():
        raise ValueError("Input text must not be empty.")
    
    classifier = get_classifier()
    result = classifier(text)[0]

    return {
        "text": text,
        "label": result["label"].lower(),
        "score": float(result["score"])
    } """

from transformers import pipeline

MODEL_NAME = "cardiffnlp/twitter-roberta-base-sentiment-latest"

_classifier = None

def get_classifier():
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "sentiment-analysis",
            model=MODEL_NAME,
            tokenizer=MODEL_NAME
        )
    return _classifier

def predict_sentiment(text: str) -> dict:
    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")
    
    if not text.strip():
        raise ValueError("Input text must not be empty.")
    
    classifier = get_classifier()
    result = classifier(text)[0]

    return {
        "text": text,
        "label": result["label"].lower(),
        "score": float(result["score"])
    }