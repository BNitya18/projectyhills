# data_collection.py
import tweepy
import pandas as pd

def collect_tweets(api_key, api_key_secret, access_token, access_token_secret, query, count):
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    tweets = []
    for tweet in tweepy.Cursor(api.search_tweets, q=query, lang="en").items(count):
        tweets.append(tweet.text)
    df = pd.DataFrame(tweets, columns=['text'])
    df.to_csv('data/tweets.csv', index=False)

# Example Usage:
# collect_tweets('api_key', 'api_key_secret', 'access_token', 'access_token_secret', 'stock market', 100)
