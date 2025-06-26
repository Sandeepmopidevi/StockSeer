from flask import Flask, request, jsonify
from flask_cors import CORS
from data_fetcher import fetch_stock_data
from feature_engineer import add_features
from xgb_model import train_xgb
from lstm_model import prepare_lstm_data, build_lstm
from hybrid_predictor import hybrid_predict, compute_rmse
import numpy as np
import threading
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

app = Flask(__name__)
CORS(app)

stock_cache = {}
model_cache = {}

def get_stock_data_cached(ticker):
    if ticker not in stock_cache:
        stock_cache[ticker] = fetch_stock_data(ticker)
    return stock_cache[ticker].copy()

def train_models_for_ticker(ticker):
    if ticker in model_cache:
        return model_cache[ticker]

    df = get_stock_data_cached(ticker)
    df = add_features(df)

    # 52-week stats
    close_prices = df['Close'].dropna().tail(252)
    high_52week = float(close_prices.max().item())
    low_52week = float(close_prices.min().item())


    # Train XGBoost
    xgb_model, xgb_preds, y_test_xgb, xgb_rmse = train_xgb(df)

    # Train LSTM
    close_values = df[['Close']].values
    X_lstm, y_lstm, scaler = prepare_lstm_data(close_values)
    split = int(0.8 * len(X_lstm))
    X_train_lstm, X_test_lstm = X_lstm[:split], X_lstm[split:]
    y_train_lstm, y_test_lstm = y_lstm[:split], y_lstm[split:]

    lstm_model = build_lstm(X_train_lstm, y_train_lstm)
    lstm_preds = lstm_model.predict(X_test_lstm, verbose=0)
    lstm_preds_scaled = scaler.inverse_transform(lstm_preds)

    # Combine
    final_preds = hybrid_predict(xgb_preds, lstm_preds_scaled)
    final_rmse = compute_rmse(y_test_lstm, final_preds)

    result = {
        "ticker": ticker,
        "final_preds": final_preds,
        "rmse": final_rmse,
        "high_52week": high_52week,
        "low_52week": low_52week
    }

    model_cache[ticker] = result
    return result

@app.route("/predict", methods=["GET"])
def predict():
    ticker = request.args.get("ticker", default="AAPL")
    try:
        result = train_models_for_ticker(ticker)

        final_preds = result["final_preds"]
        final_rmse = result["rmse"]
        high_52week = result["high_52week"]
        low_52week = result["low_52week"]

        suggestion = "Yes, it's a good time to invest." if final_preds[-1] > final_preds[-5] else "No, wait for a better entry."

        return jsonify({
            "ticker": ticker,
            "prediction": [round(float(p), 2) for p in final_preds[-10:]],
            "latest_predicted_price": round(float(final_preds[-1]), 2),
            "rmse": round(float(final_rmse), 2),
            "suggestion": suggestion,
            "high_52week": round(high_52week, 2),
            "low_52week": round(low_52week, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    # Warm up common tickers
    for t in ["AAPL", "GOOG", "TSLA", "MSFT", "AMZN"]:
        threading.Thread(target=train_models_for_ticker, args=(t,)).start()

    app.run(debug=True)
