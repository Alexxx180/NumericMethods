import numpy as np
from scipy.integrate import odeint

""" Task A """
class FormulaA:
    @staticmethod
    def formula(x, y):
        return y / (1 + pow(x, 2))

    @staticmethod
    def analyze(x: float): # Аналитическое решение
        return np.exp(((x ** 3) / 3) + x) - 1

    @staticmethod
    def diff_eq(y, x): # Уравнение с разделяющимися переменными
        return (1 + x ** 2) * (1 + y)

    # Интегрирование уравнения
    @staticmethod
    def integrate(precision: float, x: float, y0: float):
        return odeint(diff_eq, y0, x, rtol=precision, atol=precision)


""" Task B """
class FormulaB:
    @staticmethod
    def sin(x):
       return np.sin(x)

    @staticmethod
    def exp(x):
        return np.exp(-x)

    @staticmethod
    def cos(x):
        return np.cos(x)

    tasks = (sin, exp, cos)

    @staticmethod
    def epsilon(res1: iterable, res2: iterable):
        result = []
        n = len(res1)
        for i in range(n):
            difference = float(res2[i]) - float(res1[i])
            result.append(abs(difference))
        return result
