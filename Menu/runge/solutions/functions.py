import numpy as np
from scipy.integrate import odeint
from functools import reduce
from operator import sub

Precision = 1e-9

def kl_order(h: float) -> list:
    return [1, [[h, h] for i in range(4)]]

def calculate(k: tuple, l: int) -> float:
    return (k[1][l] + k[2][l] * 2 + k[3][l] * 2 + k[4][l]) / 6

def derivative(self, y: list, a: float, b: float, fx: callable) -> float:
    f = (fx, lambda d: b * d, lambda d1: a * d1) # y'' = a * y' + b * y + f(x)
    return sum([f[i](y[i]) for i in range(0, len(f))])

def function1(y: list, a: float, b: float, n: int) -> list:
    result: list = []
    for i in range(n + 1):
        r: list = [1, a, b]
        for ii in range(3, 1, -1):
            r[ii] *= y[ii][i]

        result.append(reduce(sub, r))
    return result

def function2(f: callable, x: list, n: int) -> list:
    return [f(x[i]) for i in range(n + 1)]

def analyze(x: float):
    return np.exp(((x ** 3) / 3) + x) - 1

def diff_equation(y, x):
    return (1 + x ** 2) * (1 + y)

def integrate(x: list, y0: float):
    return odeint(diff_equation, y0, x, rtol=Precision, atol=Precision)

def epsilon(r: list):
    n = len(r[0])
    return [abs(float(r[1][i]) - float(r[0][i])) for i in range(n)]
