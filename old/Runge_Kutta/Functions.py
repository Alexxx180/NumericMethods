import numpy as np
from math import sqrt

class B:
    def __init__(self, a, b, n, h, x_0, y_0, yp_0):
        ic()  # noqa: F821
        self.a = a
        self.b = b
        self.n = n
        self.h = h
        self.x_0 = x_0
        self.y_0 = y_0
        self.yp_0 = yp_0

    def f_1(self, ypp, yp, y):
        r = []
        for i in range(self.n + 1):
            ic(i)  # noqa: F821
            res = ypp[i] - self.a * yp[i] - self.b * y[i]
            r.append(res)
        return r

    def f_2(self, x, f):
        r = []
        for i in range(self.n + 1):
            res = f(x[i])
            r.append(res)
        return r

    def f(self, x, y, u, f_0):
        return self.a * u + self.b * y + f_0(x)  # u' = a*u + b*y + f(x)

    # Метод Рунге-Кутта четвёртого порядка
    def runge_kutta(self, g):
        f = self.f
        n = self.n
        h = self.h
        x = self.x_0
        y = self.y_0
        u = self.yp_0
        X = [x]
        Y = [y]
        U = [u]
        Up = [f(x, y, u, g)]

        for i in range(n):
            k1 = h * u
            l1 = h * f(x, y, u, g)

            k2 = h * (u + l1 / 2)
            l2 = h * f(x + h / 2, y + k1 / 2, u + l1 / 2, g)

            k3 = h * (u + l2 / 2)
            l3 = h * f(x + h / 2, y + k2 / 2, u + l2 / 2, g)

            k4 = h * (u + l3)
            l4 = h * f(x + h, y + k3, u + l3, g)

            y += (k1 + 2 * k2 + 2 * k3 + k4) / 6
            u += (l1 + 2 * l2 + 2 * l3 + l4) / 6
            x += h

            up = f(x, y, u, g)

            X.append(x)
            Y.append(y)
            U.append(u)

            Up.append(up)

        return X, Y, U, Up

""" TASK A BELOW """

def g1(x):
    return np.sin(x)


def g2(x):
    return np.exp(-x)


def g3(x):
    return np.cos(x)


def func_a(x, y):
	return y / (1 + pow(x,2)) # FORMULA


def epsilon(res1, res2):
    n = len(res1)
    r = []
    for i in range(n):
        res = float(res2[i]) - float(res1[i])
        r.append(abs(res))
    return r


# Уравнение с разделяющимися переменными
def diff_eq(y, x):
    return (1 + x ** 2) * (1 + y)


# Аналитическое решение
def analytical_solution(x):
    return np.exp(((x ** 3) / 3) + x) - 1


def format_list(format, list):
    new_list = [format.format(num) for num in list]
    return new_list


def metod(f, x_0, y_0, h, n):
    x = np.zeros(n + 1)
    y = np.zeros(n + 1)
    x[0], y[0] = x_0, y_0

    for i in range(1, n + 1):
        k1 = h * f(x[i - 1], y[i - 1])
        k2 = h * f(x[i - 1] + h / 2, y[i - 1] + k1 / 2)
        k3 = h * f(x[i - 1] + h / 2, y[i - 1] + k2 / 2)
        k4 = h * f(x[i - 1] + h, y[i - 1] + k3)

        y[i] = y[i - 1] + (k1 + 2 * k2 + 2 * k3 + k4) / 6
        x[i] = x[i - 1] + h
    return x, y
