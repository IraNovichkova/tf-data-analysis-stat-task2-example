import pandas as pd
import numpy as np


chat_id = 335933917 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    alpha = 1 - p
    return np.amax(x), (np.amax(x) - 0.098) / (alpha**(1 / len(x))) + 0.098
