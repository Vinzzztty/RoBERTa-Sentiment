from flask import Flask, request, jsonify
from src import roberta_model

app = Flask(__name__)


@app.route('/')
def main():
    return "<h1>Hello API </h1>"

@app.route('/analyze', methods=['POST'])
def sentiment_analyze():
    try:
        data = request.get_json()
        text = data['text']
    
        result = roberta_model.analyze_sentiment(dataframe=text)

        return jsonify({
            'label': result[0]['label'],
            'score': result[0]['score']
        }), 200

    except Exception as e:
        return jsonify({
            'error': str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True, port=8001)
