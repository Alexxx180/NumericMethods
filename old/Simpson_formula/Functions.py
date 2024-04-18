import numpy as np
from Classes.Points import PointGraphs
from Classes.Table import Table
from Classes.Input import UserSelect

class func:
    def __init__(self, a, b):
        self.a = a
        self.b = b

#    def func_1(self, x):

#"""
    def func_1(self, x):
        return np.exp(self.a * x) * np.sin(self.b * x)

    def func_2(self, x):
        return 1 / np.sqrt(x ** 2 + self.a)

    def func_1_4d(self, x):
        res = self.a ** 4 * np.sin(self.b * x)
        res += 4 * self.a ** 3 * self.b * np.cos(self.b * x)
        res -= 6 * self.a ** 2 * self.b ** 2 * np.sin(self.b * x)
        res -= 4 * self.a * self.b ** 3 * np.cos(self.b * x)
        res += self.b ** 4 * np.sin(self.b * x)
        res *= np.exp(self.a * x)
        return res

    def func_2_4d(self, x):
        a = (35*x**4) / ((self.a+x**2)**2)
        b = (30*x**2) / (self.a+x**2)
        a_b = a - b + 3
        a_b *= 3
        res = a_b/((self.a +x**2)**(5/2))
        #res = ((35 * x ** 4) / (self.a + x ** 2) ** 2) - ((30 * x ** 2) / (self.a + x ** 2) + 3)
        #res *= 3
        #res /= (self.a + x ** 2) ** (5 / 2)
        return res
 #   """


def line(x, f, ax):
    # 'ro' рисует красную точку в координатах (x, y)
    drawing = 'ro'
    horizontal = 'left'
    vertical = 'bottom'
    font = 12

    result = f(x)
    basis = 0

    ax.vlines(x, basis, result,
        colors="red", linestyles='dashed')
    ax.plot(x, result, drawing)
    ax.plot(x, basis, drawing)

    if abs(result) > 0.01:
        # Добавляем текст
        ax.text(x, result, f"{f(x):.2f}", fontsize=font,
                ha=horizontal, va=vertical)

        ax.text(x, basis, f"{x:.2f}", fontsize=font,
                ha=horizontal, va=vertical)

def define_m(start, end, f, ax):
    points = PointGraphs(start, end, f)
    # Нахождение максимального значения
    y = points.Y
    x = points.X

    mp = map(abs, y)
    mx = max(mp)

    pts = enumerate(y)
    indices = [index for index, value in pts if abs(value) == mx]
    ic(indices) ; ic(mx)  # noqa: F821

    #index = x_y.Y.index(mx)
    i = int(indices[0])
    line(x[i], f, ax)

    return mx


def define_n(start, end, m, e):
    # ^0.25 корень 4 степени
    size = end - start
    d = 180 * e
    n = m * size ** 5 / d
    ic(n)  # noqa: F821

    d = 1 / 4
    n = n ** d

    if not isinstance(n, int):
        n = int(n + 1)

    while n % 2 != 0:
        n += 1
        
    return n


def s_f(start, end, n, f, ax):
    # Поля таблицы
    fields = ["i", "xᵢ", "i = 0, n", "xᵢ четное", "xᵢ нечетное"]
    table = Table(fields, "Результаты") ; ic()  # noqa: F821
    
    # Крайние значения
    y_start = f(start)
    y_end = f(end)

    h = end - start # H в методичке
    h /= n
    print(f"h = {h}") ; ic(h)  # noqa: F821

    middle = y_start - y_end # S в методичке
    middle /= 2 ; ic(middle) ; ic(n // 2)  # noqa: F821

    result = y_start + y_end
    none = "-"
    miss = ""

    rows = []
    rows.append([start, y_start, none, none])

    line(start, f, ax)
    line(end, f, ax)

    factors = [2, 4]

    for i in range(1, n):
        x = start + i * h
        line(x, f, ax)
        y = f(x)

        current = i % 2
        factor = factors[current]
        result += factor * y

        records = [[miss, y], [y, none]]
        row = [x, none]
        row.extend(records[current])
        rows.append(row)

    rows.append([end, y_end, none, none])
    table.add_row(rows)

    query = "Показать таблицу расчетов? (y/n)"

    if n <= 15 or UserSelect(query):
        table.show()

    return h / 3 * result
