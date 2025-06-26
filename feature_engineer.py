import pandas as pd
def add_features(df):
    close = df['Close']

    if isinstance(close, pd.DataFrame):
        close = close.squeeze()  # Ensure it's a Series

    df['MA5'] = close.rolling(window=5).mean()
    df['MA20'] = close.rolling(window=20).mean()
    df['RSI'] = compute_rsi(close, 14)

    df.dropna(inplace=True)
    return df

def compute_rsi(series, period=14):
    delta = series.diff()
    gain = delta.where(delta > 0, 0).rolling(window=period).mean()
    loss = -delta.where(delta < 0, 0).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))
