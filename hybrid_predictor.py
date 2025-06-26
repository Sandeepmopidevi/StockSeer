import numpy as np
from sklearn.metrics import mean_squared_error

def hybrid_predict(xgb_preds, lstm_preds):
    min_len = min(len(xgb_preds), len(lstm_preds))
    hybrid = (np.array(xgb_preds[:min_len]) + np.array(lstm_preds[:min_len].flatten())) / 2
    return hybrid

def compute_rmse(y_true, y_pred):
    y_true = y_true[:len(y_pred)]
    return np.sqrt(mean_squared_error(y_true, y_pred))
