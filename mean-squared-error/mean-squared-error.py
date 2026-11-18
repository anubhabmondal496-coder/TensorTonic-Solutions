import numpy as np

def mean_squared_error(y_pred: list, y_true: list) -> float:
    sum = 0
    n = len(y_pred)
    for i in range(0,n):
        sum += pow((y_pred[i] - y_true[i]),2)

    mse = sum / n

    return mse