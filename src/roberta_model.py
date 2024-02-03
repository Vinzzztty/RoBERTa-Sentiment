from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

def analyze_sentiment(dataframe):

    # Tokenizer and Model
    tokenizer = AutoTokenizer.from_pretrained("w11wo/indonesian-roberta-base-sentiment-classifier")
    model = AutoModelForSequenceClassification.from_pretrained("w11wo/indonesian-roberta-base-sentiment-classifier")

    nlp = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer
    )

    return nlp(dataframe)