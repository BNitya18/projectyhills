# time_series_analysis.py
import yfinance as yf
import pandas as pd

def get_stock_data(ticker, start_date, end_date):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    return stock_data[['Date', 'Close']]

def merge_data(stock_file, sentiment_file, output_file):
    stock_data = pd.read_csv(stock_file)
    sentiment_data = pd.read_csv(sentiment_file)
    combined_data = pd.merge(stock_data, sentiment_data, left_on='Date', right_on='Date', how='inner')
    combined_data.to_csv(output_file, index=False)

# Example Usage:
# stock_data = get_stock_data("AAPL", "2023-01-01", "2024-01-01")
# stock_data.to_csv('data/stock_data.csv', index=False)
# merge_data('data/stock_data.csv', 'data/labeled_tweets.csv', 'outputs/combined_data.csv')
