# src/data_loader.py

import pandas as pd

def load_data(sentiment_path, trades_path):
    #Load both datasets
    sentiment = pd.read_csv(sentiment_path)
    trades = pd.read_csv(trades_path)

    return sentiment, trades