import pandas as pd
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import random

def analyze_sentiment(df):
    # Tokenize and analyze sentiment
    tokenizer = AutoTokenizer.from_pretrained("w11wo/indonesian-roberta-base-sentiment-classifier")
    model = AutoModelForSequenceClassification.from_pretrained("w11wo/indonesian-roberta-base-sentiment-classifier")

    nlp = pipeline(
        "sentiment-analysis",
        model=model,
        tokenizer=tokenizer
    )

    # Select a random subset of 100 rows
    random_rows = random.sample(range(len(df)), min(100, len(df)))
    df_subset = df.iloc[random_rows]

    # Analyze sentiment for each row in the subset
    results = []
    for index, row in df_subset.iterrows():
        result = nlp(row['title'])
        results.append(result[0]['label'])  # Extract the sentiment result from the list

    return df_subset, results

def save_sentiment_results(df, results, output_csv):
    # Add a new column 'predict' to the DataFrame
    df['predict'] = results

    # Convert the DataFrame to JSON and save to CSV
    df.to_csv(output_csv, index=False)

# Example usage
df = pd.read_csv('./test/data_berita.csv')
new_df = df[['title']].copy()

# Analyze sentiment and save results for a random subset of 100 rows
subset_df, sentiment_results = analyze_sentiment(new_df)

# Save the sentiment analysis results to a new CSV file
output_csv = './test/data_berita_random_subset_with_predictions.csv'
save_sentiment_results(subset_df, sentiment_results, output_csv)
