
from sklearn.metrics import mean_absolute_error, mean_squared_error
import time
import numpy as np




def compute_rmse(y_pred, y_true):
    return np.sqrt(((y_pred - y_true)**2).mean())



def compute_mae(y_pred, y_true):
    return mean_absolute_error(y_pred, y_true)

def compute_mse(y_pred, y_true):
    return mean_squared_error(y_pred, y_true)
