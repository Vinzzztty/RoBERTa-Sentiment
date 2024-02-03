from flask import Flask
from src import roberta_model

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello API </h1>"

@app.route('/analyze')
def sentiment_analyze():
    word = "Aku senang sekali hari ini"

    result = roberta_model.analyze_sentiment(dataframe=word)

    return result


if __name__ == '__main__':
    app.run(debug=True, port=8001)
