import numpy as np
from math import log10


# def f(x):
#    return ((x - 2) ** 2 - 1) * 2 ** x - 1

def f(x):
    return x ** 4 - x - 1


def line(x, color, ax):
    ax.vlines(x, 0, f(x), colors=color, linestyles='dashed')
    ax.plot(x, f(x), 'ro')  # 'ro' рисует красную точку в координатах (x, y)
    ax.plot(x, 0, 'ro')  # 'ro' рисует красную точку в координатах (x, y)
    if abs(f(x)) > 0.01:
        ax.text(x, f(x), f"{f(x):.2f}", fontsize=12, ha='left', va='bottom')  # Добавляем текст
        ax.text(x, 0, f"{x:.2f}", fontsize=12, ha='left', va='bottom')  # Добавляем текст


def study_function(a, b, n, ax):
    ic(a, b, n)  # noqa: F821
    print("")
    print("Запуск исследования функции")
    print(f'исследуем интервал от {a} до {b}')
    step = (b - a) / n  # Вычисляем шаг разбиения
    intervals_with_roots = []  # Список отрезков, предположительно содержащих корни
    previous_x = a
    previous_sign = f(a)

    for i in np.arange(1, n + 1, 1):
        current_x = a + i * step
        current_sign = f(current_x)
        # Проверяем изменение знака
        if current_sign * previous_sign <= 0:  # Если знак функции изменился или равен нулю
            # print(f"{previous_x, current_x} - корень есть")
            intervals_with_roots.append((previous_x, current_x))
            line(previous_x, "blue", ax)
            line(current_x, "blue", ax)
        else:
            # print(f"{previous_x, current_x} - знак не сменился ищем дальше")
            line(previous_x, "red", ax)
            line(current_x, "red", ax)

        # Переходим к следующему подотрезку
        previous_x = current_x
        previous_sign = current_sign

    if len(intervals_with_roots) == 0:
        return None
    return intervals_with_roots


def breakdown(x_1, x_2, e, ax):
    while (x_2 - x_1) > 2 * e:
        line(x_1, "green", ax)
        line(x_2, "green", ax)
        c = (x_1 + x_2) / 2  # середина отрезка [a, b]
        if f(x_1) * f(c) > 0:
            x_1 = c
        else:
            x_2 = c
            # [a, c] или [c, b] ?
        print(f"[{x_1}, {x_2}]")
    line(x_1, "green", ax)
    line(x_2, "green", ax)
    print(f"[{x_1}, {x_2}]")
    return x_1, x_2
