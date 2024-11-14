# main.py
from scripts.data_collection import collect_tweets
from scripts.data_preprocessing import preprocess_data
from scripts.sentiment_model import analyze_sentiments
from scripts.time_series_analysis import get_stock_data, merge_data

def main():
    # Step 1: Data Collection
    collect_tweets('api_key', 'api_key_secret', 'access_token', 'access_token_secret', 'stock market', 100)
    
    # Step 2: Data Preprocessing
    preprocess_data('data/tweets.csv', 'data/cleaned_tweets.csv')
    
    # Step 3: Sentiment Analysis
    analyze_sentiments('data/cleaned_tweets.csv', 'data/labeled_tweets.csv')
    
    # Step 4: Time-Series Analysis
    stock_data = get_stock_data("AAPL", "2023-01-01", "2024-01-01")
    stock_data.to_csv('data/stock_data.csv', index=False)
    merge_data('data/stock_data.csv', 'data/labeled_tweets.csv', 'outputs/combined_data.csv')

if __name__ == "__main__":
    main()
