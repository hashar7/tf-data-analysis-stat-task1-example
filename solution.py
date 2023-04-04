import pandas as pd
import numpy as np


chat_id = 458704720 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    return 2 * np.median(x) / (42 ** 2)
