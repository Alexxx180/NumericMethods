import numpy as np

from math import tan, sin, cos


global_float_format = "{:.8f}"


def f_a(x):
    """ Функция а """
    return x ** 3 + 0.2 * x ** 2 + 0.5 * x - 2 # FORMULA A


def f_a_s(x):
    """ Производная Функция а' """
    return 3 * x ** 2 + 0.4 * x + 0.5


def f_a_s_s(x):
    """ Производная Функция а'' """
    return 6 * x + 4


def f_b(x):
    """ Функция b """

    return tan(0.5 * x + 0.1) - x ** 2

def f_b_s(x):
    """ Производная Функция b' """

    d = cos(0.5 * x + 0.1) ** 2
    if d == 0:
        return 0

    return 1 / d - 2 * x

def f_b_s_s(x):
    """ Производная Функция b'' """

    x1 = 0.5 * x + 0.1
    xs = sin(x1)
    xc = cos(x1)
    return 2 * xs * xc


def tangent_g(r, ax):
    # Задание длины линии касательной
    line_length = 100
    for index, num in enumerate(r):
        x_point = float(num[0])
        y_point = float(num[1])
        f_prime = float(num[2])

        # Генерация точек для графика функции
        x_values = np.linspace(x_point - line_length / 2, x_point + line_length / 2, 100)
        # Рисование касательной
        tangent_line = f_prime * (x_values - x_point) + y_point

        ax.plot(x_values, tangent_line, label='Касательная {}'.format(index), linestyle='--')
        ax.scatter(x_point, y_point, color='red', label='её точка')


def research(a, b, f, df, ddf):
    ic()  # noqa: F821
    m = min(abs(df(a)), abs(df(b)))

    if f(a) * f(b) < 0:
        if f(a) * ddf(a) > 0:
            if df(a) != 0 or ddf(a) != 0:
                return a, m
            else:
                return None, f"f`(a) = {df(a)},f``(a) = {ddf(a)} "
        elif f(b) * df(b) > 0:
            if df(b) != 0 or ddf(b) != 0:
                return b, m
            else:
                return None, f"f`(b) = {df(b)},f``(b) = {ddf(b)} "
    else:
        return None, f"f(a) * f(b) = {f(a)} * {f(b)} = {f(a) * f(b)} > 0"


def tangent(e, m, x, f, df):
    r = []
    while (abs(f(x)) / m) > e:
        ic(global_float_format.format(abs(f(x)) / m))  # noqa: F821
        ic(global_float_format.format(e))  # noqa: F821
        x_1 = x - f(x) / df(x)
        r.append(
            [global_float_format.format(x), global_float_format.format(f(x)), global_float_format.format(df(x)),
             global_float_format.format(abs(f(x)) / m)])
        x = x_1
    if (abs(f(x)) / m) == 0:
        r.append(
            [global_float_format.format(x), global_float_format.format(f(x)), global_float_format.format(df(x)),
             0])
    else:
        r.append(
            [global_float_format.format(x), global_float_format.format(f(x)), global_float_format.format(df(x)),
             abs(f(x)) / m])
    return r
