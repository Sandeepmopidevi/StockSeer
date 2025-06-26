from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np

def train_xgb(df):
    df = df.copy()
    df = df.dropna()
    features = ['MA5', 'MA20', 'RSI']
    X = df[features]
    y = df['Close']
    X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

    model = XGBRegressor(n_estimators=100, max_depth=4)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, preds))
    return model, preds, y_test, rmse
