import pandas as pd

def evaluate_regression(y_true, y_pred) -> dict:
    from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
    import numpy as np
    mae = mean_absolute_error(y_true, y_pred)
    rmse = mean_squared_error(y_true, y_pred, squared=False)
    r2 = r2_score(y_true, y_pred)
    mape = float((abs((y_true - y_pred) / y_true)).replace([float('inf')], None).dropna().mean()) if isinstance(y_true, pd.Series) else None
    return {"MAE": mae, "RMSE": rmse, "R2": r2, "MAPE": mape}
