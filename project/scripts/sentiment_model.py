# sentiment_model.py
from transformers import pipeline
import pandas as pd

def sentiment_analysis(text):
    classifier = pipeline("sentiment-analysis")
    return classifier(text)[0]['label']

def analyze_sentiments(input_file, output_file):
    df = pd.read_csv(input_file)
    df['sentiment'] = df['cleaned_text'].apply(sentiment_analysis)
    df.to_csv(output_file, index=False)

# Example Usage:
# analyze_sentiments('data/cleaned_tweets.csv', 'data/labeled_tweets.csv')
