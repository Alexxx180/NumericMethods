import numpy as np
from scipy.integrate import odeint

Precision = 1e-9

""" Task A """
def analyze(x: float): # Аналитическое решение
    return np.exp(((x ** 3) / 3) + x) - 1

def diff_equa(y, x):
    return (1 + x ** 2) * (1 + y)

# Интегрирование уравнения
def integrate(x: float, y0: float):
    return odeint(diff_eq, y0, x, rtol=Precision, atol=Precision)

""" Task B """
def epsilon(res1, res2):
    result = []
    n = len(res1)
    for i in range(n):
        difference = float(res2[i]) - float(res1[i])
        result.append(abs(difference))
    return result
