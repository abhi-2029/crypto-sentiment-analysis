# main.py

import os

from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import (
    sentiment_profit_analysis,
    win_rate_analysis,
    trade_count_analysis,
    leverage_analysis,
    side_analysis,
    volatility_analysis
)
from src.visualization import plot_profit_distribution, plot_win_rate



# output folder Creation

os.makedirs("output/plots", exist_ok=True)



# Load data
print("\n Loading datasets...")
sentiment, trades = load_data(
    "data/fear_greed_index.csv",
    "data/historical_data.csv"
)

print("Data Loaded Successfully")



#  DEBUG: Check columns Before preprocessing

print("\n Trades Columns:")
print(trades.columns)

print("\n First 5 rows of trades:")
print(trades.head())

print("\n Sentiment Columns:")
print(sentiment.columns)



# Preprocess data

print("\n Preprocessing data...")
df = preprocess_data(sentiment, trades)

print(" Preprocessing Done")



#  Verify Merge

print("\n Checking merged data sample...")
print(df[['Date', 'closedPnL', 'Classification']].head())

print("\n Checking missing sentiment values...")
missing = df['Classification'].isna().sum()
print(f"Missing Sentiment Values: {missing}")



# Perform analysis

print("\n Running analysis...")

profit = sentiment_profit_analysis(df)
win_rate = win_rate_analysis(df)
trade_count = trade_count_analysis(df)
leverage = leverage_analysis(df)
side = side_analysis(df)
volatility = volatility_analysis(df)



# Print results

print("\n=== Profit by Sentiment ===")
print(profit)

print("\n=== Win Rate ===")
print(win_rate)

print("\n=== Trade Count ===")
print(trade_count)

print("\n=== Leverage ===")
print(leverage)

print("\n=== Long/Short Performance ===")
print(side)

print("\n=== Volatility ===")
print(volatility)



# plots generations

print("\n Generating plots...")
plot_profit_distribution(df)
plot_win_rate(win_rate)


# Save report

print("\n Saving report...")

with open("output/report.txt", "w") as f:
    f.write("=== Crypto Sentiment Analysis Report ===\n\n")

    f.write("Merged Data Sample:\n")
    f.write(str(df[['Date', 'closedPnL', 'Classification']].head()) + "\n\n")

    f.write("Missing Sentiment Values:\n")
    f.write(str(missing) + "\n\n")

    f.write("Profit by Sentiment:\n")
    f.write(str(profit) + "\n\n")

    f.write("Win Rate:\n")
    f.write(str(win_rate) + "\n\n")

    f.write("Trade Count:\n")
    f.write(str(trade_count) + "\n\n")

    f.write("Leverage:\n")
    f.write(str(leverage) + "\n\n")

    f.write("Side Analysis:\n")
    f.write(str(side) + "\n\n")

    f.write("Volatility:\n")
    f.write(str(volatility) + "\n\n")


print("\n Analysis Complete. Check output folder.")