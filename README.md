# Sentiment Analysis API use RoBERTa

This API allows you to perform sentiment analysis on a given text using a pre-trained model. The API is built with Flask and supports POST requests for text analysis.

## How to Use

Install dependencies

```
pip install -r requirements.txt
```

Run the Flask Server

```
python app.py
```

Example API <br>
Analyze Sentiment
Send a POST request to the `/analyze` endpoint with a JSON payload containing the text you want to analyze.

```
{
    "text": "Aku senang sekali hari ini"
}
```
