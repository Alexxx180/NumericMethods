import numpy as np
from scipy.integrate import odeint
from functools import reduce
from operator import sub

Precision = 1e-9

def kl_order(h: float) -> list:
    kl: list = [1]
    for i in range(4):
        kl.append([h, h])
    return kl

def calculate(k: tuple, l: int) -> float:
    return (k[1][l] + k[2][l] * 2 + k[3][l] * 2 + k[4][l]) / 6

def derivative(y: list, a: float, b: float, f: callable) -> float:
    return a * y[2] + b * y[1] + f(y[0]) # y'' = a * y' + b * y + f(x)

def function1(y: list, a: float, b: float, n: int) -> list:
    return [y[2][i] * a - y[1][i] * b - y[0][i] for i in range(n)]

def function2(f: callable, x: list, n: int) -> list:
    return [f(x[i]) for i in range(n)]

def epsilon(r: list, n: int) -> list:
    return [abs(float(r[1][i]) - float(r[0][i])) for i in range(n)]

def analyze(x: list) -> list:
    return np.exp(((x ** 3) / 3) + x) - 1

def diff_equation(y, x):
    return (1 + x ** 2) * (1 + y)

def integrate(x: list, y0: float):
    return odeint(diff_equation, y0, x, rtol=Precision, atol=Precision)
