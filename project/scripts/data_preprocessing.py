# data_preprocessing.py
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

def preprocess_text(text):
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)
    text = re.sub(r'\@\w+|\#', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.lower()
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word not in stopwords.words('english')]
    return ' '.join(tokens)

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)
    df['cleaned_text'] = df['text'].apply(preprocess_text)
    df.to_csv(output_file, index=False)

# Example Usage:
# preprocess_data('data/tweets.csv', 'data/cleaned_tweets.csv')
