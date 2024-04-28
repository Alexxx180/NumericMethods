import numpy as np
from scipy.integrate import odeint

Precision = 1e-9

""" Task A """
def analyze(x: float): # Аналитическое решение
    return np.exp(((x ** 3) / 3) + x) - 1

def diff_equation(y, x):
    return (1 + x ** 2) * (1 + y)

# Интегрирование уравнения
def integrate(x: float, y0: float):
    return odeint(diff_equation, y0, x, rtol=Precision, atol=Precision)

""" Task B """
def epsilon(result: tuple):
    result = []
    n = len(result[0])
    for i in range(n):
        difference = float(result[1][i]) - float(result[0][i])
        result.append(abs(difference))
    return result
