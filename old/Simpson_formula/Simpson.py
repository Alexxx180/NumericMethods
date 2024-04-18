from Simpson_formula.Functions import s_f, define_n, define_m, func
from Classes.Graphs import Graphs
from Classes.Points import PointGraphs
from hendllers.func import pause

plot = None

def Calculate(start, end, e, f_main, f_4d):
    global plot
    axis1 = plot.ax[0]
    axis2 = plot.ax[1]

    m = define_m(start, end, f_4d, axis2)
    # функция 4 той производной
    print(f"M = {m}") ; ic(m) # noqa: F821

    n = define_n(start, end, m, e)
    print(f"n = {n}") ; ic(n) ; ic()  # noqa: F821

    s = s_f(start, end, n, f_main, axis1)
    ic(s)  # noqa: F821

    x = start - 10
    y = end + 10

    point_1 = PointGraphs(x, y, f_main)
    point_2 = PointGraphs(x, y, f_4d)

    plot.Creating_graph_more(0, point_1.X, point_1.Y)
    plot.Creating_graph_more(1, point_2.X, point_2.Y)
    return s

def Simpson(a, b, start, end, e):
    global plot
    # a = 0.64, b = 1.19
    # пределы интегрирования
    # start = 1, end = 2

    print(f"a = {a}")
    print(f"b = {b}")
    print(f"e = {e:.15f}")

    print(f"Пределы интегрирования от {start} до {end}")

    x = start - 0.5
    y = end + 0.5
    at = -10
    to = 10

    plot = Graphs(1,2)
    plot.settings_more(0, "График f(x)", x, y, at, to)
    plot.settings_more(1, "График f````(x)", x, y, at, to)

    f = func(a, b)

    if b is not None:
        s = Calculate(start, end, e, f.func_1, f.func_1_4d)
    else:
        s = Calculate(start, end, e, f.func_2, f.func_2_4d)

    print(f"Значениие интергала равно: {s}")
    pause()
    # plot.show() # График
