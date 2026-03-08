from unittest.mock import patch
import pytest
from src.predict import predict_sentiment

@patch("src.predict.get_classifier")
def test_predict_sentiment_returns_dict(mock_get_classifier):
    mock_get_classifier.return_value = lambda text: [
        {"label": "positive", "score": 0.98}
    ]
    result = predict_sentiment("I love this product!")
    assert isinstance(result, dict)

@patch("src.predict.get_classifier")
def test_predict_sentiment_contains_keys(mock_get_classifier):
    mock_get_classifier.return_value = lambda text: [
        {"label": "positive", "score": 0.98}
    ]
    result = predict_sentiment("This is amazing!")
    assert "text" in result
    assert "label" in result
    assert "score" in result

@patch("src.predict.get_classifier")
def test_predict_sentiment_label_is_valid(mock_get_classifier):
    mock_get_classifier.return_value = lambda text: [
        {"label": "negative", "score": 0.91}
    ]
    result = predict_sentiment("This is terrible.")
    assert result["label"] in ["positive", "neutral", "negative"]

@patch("src.predict.get_classifier")
def test_predict_sentiment_score_range(mock_get_classifier):
    mock_get_classifier.return_value = lambda text: [
        {"label": "neutral", "score": 0.75}
    ]
    result = predict_sentiment("The update was released today.")
    assert 0.0 <= result["score"] <= 1.0

def test_predict_sentiment_empty_string():
    with pytest.raises(ValueError):
        predict_sentiment("")

def test_predict_sentiment_non_string():
    with pytest.raises(TypeError):
        predict_sentiment(123)