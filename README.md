# 📈 StockSeer - Smart Investment Predictor

StockSeer is a hybrid AI-based stock price prediction system built using Flask, XGBoost, LSTM (TensorFlow/Keras), and real-time financial data via Yahoo Finance. It offers short-term stock price predictions, 52-week high/low, RMSE evaluation, and investment suggestions.

---

## 🚀 Features

- 🔮 Hybrid Prediction using XGBoost + LSTM
- 📉 Real-time Stock Data (via Yahoo Finance)
- 📊 52-Week High and Low Price Stats
- 📈 Next 10 Day Predicted Prices
- ✅ Investment Suggestion Engine
- ⏱️ Spinner and Facts while loading
- 🌐 Frontend in HTML + Vanilla JS
- ⚡ Fast caching support (multi-threading)

---

## 📁 Project Structure

```

StockSeer/
├── app.py                   # Flask API Server
├── data_fetcher.py         # Fetch stock data using yfinance
├── feature_engineer.py     # Feature engineering (MA, RSI, etc.)
├── xgb_model.py            # XGBoost model training
├── lstm_model.py           # LSTM model training
├── hybrid_predictor.py     # Combine LSTM & XGBoost predictions
├── templates/
│   └── index.html          # UI (if Flask templating used)
├── static/
│   └── tickers.js          # Company ticker mapping
├── frontend.html           # Pure frontend (JS/HTML/CSS)
└── requirements.txt        # Python dependencies

````

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sandeepmopidevi/StockSeer
cd StockSeer
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure `TensorFlow`, `pandas`, `scikit-learn`, `xgboost`, `yfinance`, and `flask` are included.

### 3. Run the Backend

```bash
python app.py
```

Flask will run on: `http://127.0.0.1:5000`

### 4. Open the Frontend

Open `frontend.html` directly in your browser. or use `python -m http.server 8080`

---

## 🧠 Tech Stack

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Flask (Python)
* **ML Models**: XGBoost, LSTM (TensorFlow)
* **Data Source**: Yahoo Finance (`yfinance`)
* **Extras**: Multithreaded caching, Spinner loader, 52-week stats

---

## 💡 Sample Use

Type a company name (e.g., `Apple Inc.`), select from suggestions, and click **Predict**.

The app will show:

* 📌 Ticker and Company Name
* 📈 Latest Predicted Stock Price
* 🔍 RMSE of Model
* 💡 Investment Suggestion (Yes/No)
* 📉 52-week High/Low
* 🔮 10-Day Forecast

---

### Sample:-

![image](https://github.com/user-attachments/assets/58248a87-716c-4597-aeda-fd2ed3019050)

---
## 🛠 Troubleshooting

* **Prediction Takes Long?**
  First run may take \~20–30s due to model training. Subsequent calls are faster with preloaded threads.

* **Invalid Company?**
  Make sure you're selecting a valid company from the dropdown.

---

## 📝 License

MIT License
---

## 👤 Author

**Sandeep Mopidevi**
Connect: [LinkedIn](https://www.linkedin.com/Sandeepmopidevi) | [YouTube](https://www.youtube.com/@TechWithSandeep)
