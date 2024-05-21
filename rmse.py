import numpy as np

def rmse(predictions, targets):
    pred = np.array(predictions)
    tar = np.array(targets)
    n = len(tar)
    rmse = np.sqrt((1 / n) * np.sum(np.square(tar - pred)))
    return rmse