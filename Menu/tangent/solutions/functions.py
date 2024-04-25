from common.calculus.trigonometry import derive

def update(y: tuple, f: callable, x: float):
    for i in range(len(y)):
        y[i] = derive(f, x, i)

def tangent(precision: float, research):
    f = research.task
    x = research.roots

    y = (0.0, 0.0)
    update(y, f, x[0])

    result = []

    a = lambda y, m: abs(y) / m

    while (n := a(y[0], x[1])) > precision:
        result.append([x[0], y[0], y[1], n])
        x[0] -= y[0] / y[1]
        update(y, f, x[0])

    update(y, f, x[0])

    row = (x[0], y[0], y[1], 0)
    if y[0] != 0:
        row[3] = a(y[0], x[1])

    result.append(row)
    return result
