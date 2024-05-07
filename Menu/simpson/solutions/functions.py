from sympy.abc import x, a, b
from common.commander.resources import Resources
from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from common.calculus.trigonometry import formulate, invokation, express
from common.drawing.drawing import *

def placeholder(x0: float):
    add = { 1: Chars['Miss'], 0: x0 }
    row = empty_list()
    for key, value in add.items():
        row.insert(key, value)
    return row

def empty_list():
    return [Chars['None'] * 2]

def determine(ab, form: str):
    task = Resources.Formula['Simpson'][form]
    if ab.end == 0:
        d1 = invokation(express(task), a, x),
        d4 = invokation(formulate(task, 4, a, x), a, x)


        return (
            lambda x0: d1(x0, ab.start),
            lambda x0: d4(x0, ab.start)
        )
    else:
        d1 = invokation(express(task), a, b, x),
        d4 = invokation(formulate(task, 4, a, b, x), a, b, x)
        print(task, ab.start)
        print('OBJECT', ab.end)

        return (
            lambda x0: d1[0](x=x0, a=ab.start, b=ab.end),
            lambda x0: d4(x=x0, a=ab.start, b=ab.end)
        )

def search_max(points: Points) -> tuple:
    maxed = max(map(abs, points.Y))
    pts = enumerate(points.Y)

    indices = [i for i, value in pts if abs(value) == maxed]
    index = int(indices[0])
    return (maxed, points.X[index])

def quadratic(size: float, m: float, e: float) -> int:
    n = (m * size ** 5 / (180 * e)) ** 0.25

    if not isinstance(n, int):
        n = int(n + 1)
    while n % 2 != 0:
        n += 1

    return n
