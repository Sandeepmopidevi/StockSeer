import yfinance as yf

def fetch_stock_data(ticker, period='2y', interval='1d'):
    df = yf.download(ticker, period=period, interval=interval)
    df.dropna(inplace=True)
    return df
