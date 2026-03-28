# src/analysis.py

def sentiment_profit_analysis(df):
    #Average profit per sentiment
    return df.groupby('Classification')['closedPnL'].mean()


def win_rate_analysis(df):
    #Win rate per sentiment
    return df.groupby('Classification')['win'].mean()


def trade_count_analysis(df):
    #Number of trades per sentiment
    return df['Classification'].value_counts()


def leverage_analysis(df):
    #Average leverage per sentiment (if available)
    if 'leverage' in df.columns:
        return df.groupby('Classification')['leverage'].mean()
    else:
        return "Leverage data not available in dataset"


def side_analysis(df):
    #Long vs Short performance
    return df.groupby(['Classification', 'side'])['closedPnL'].mean()


def volatility_analysis(df):
    #Risk (std deviation)
    return df.groupby('Classification')['closedPnL'].std()