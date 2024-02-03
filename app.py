from flask import Flask


app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello API </h1>"

@app.route('/analyze')
def sentiment_analyze():
    return 'Sentiment Analyze'


if __name__ == '__main__':
    app.run(debug=True, port=8001)
