import numpy as np
from scipy.integrate import solve_ivp
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
    return [y[3][i] - y[2][i] * a - y[1][i] * b for i in range(n)]

def function2(f: callable, x: list, n: int) -> list:
    return [f(x[i]) for i in range(n)]

def epsilon(r: list, n: int) -> list:
    return [abs(float(r[-1][i]) - float(r[-2][i])) for i in range(n)]

def analyze(h: float, x: list, y0: float, f: callable) -> list:
    solved_integral = solve_ivp(f, (x[0], x[len(x) - 1]),
        [y0], first_step=h, max_step=h)
    return solved_integral["y"][0]
