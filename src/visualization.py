# src/visualization.py

import matplotlib.pyplot as plt
import seaborn as sns
import os

def plot_profit_distribution(df):
    # Create boxplot to compare profit distribution across sentiments
    plt.figure()
    sns.boxplot(x='Classification', y='closedPnL', data=df)
    plt.title("Profit Distribution by Sentiment")
    # Save plot
    plt.savefig("output/plots/profit_distribution.png")
    plt.close()


def plot_win_rate(win_rate):
    # Create bar chart for win rate across sentiments
    plt.figure()
    win_rate.plot(kind='bar', title="Win Rate by Sentiment")
    # Save plot
    plt.savefig("output/plots/win_rate.png")
    plt.close()