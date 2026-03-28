# src/preprocessing.py

import pandas as pd

def preprocess_data(sentiment, trades):
    #Clean and prepare data (based on actual dataset structure)

   
    # SENTIMENT DATA
    sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date
    sentiment.rename(columns={
        'date': 'Date',
        'classification': 'Classification'
    }, inplace=True)


    # TRADES DATA

    # Convert timestamp (milliseconds → datetime)
    trades['Timestamp'] = pd.to_datetime(trades['Timestamp'], unit='ms')

    # Extract date
    trades['Date'] = trades['Timestamp'].dt.date

    # Rename important columns for consistency
    trades.rename(columns={
        'Closed PnL': 'closedPnL',
        'Side': 'side'
    }, inplace=True)


    # MERGE Data

    merged = pd.merge(trades, sentiment, on='Date', how='left')

    # Remove rows where sentiment is missing
    merged = merged.dropna(subset=['Classification'])


    # FEATURE ENGINEERING
    merged['win'] = merged['closedPnL'] > 0

    return merged