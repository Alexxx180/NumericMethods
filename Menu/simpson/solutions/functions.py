from common.commander.formula import *
from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from common.calculus.trigonometry import formulate, invokation, X
from common.drawing.drawing import *

def placeholder(x: float):
    add = { 1: Chars['Miss'], 0: x }
    row = empty_list()
    for key, value in add.items():
        row.insert(key, value)
    return row

def empty_list():
    return [Chars['None'] * 2]

def determine(ab, form: str):
    formula = Formula['Simpson'][form]
    if ab.end is None:
        task = formula(ab.start)
    else:
        task = formula(ab.start, ab.end)
    return (
        invokation(formulate(task, 0, X), X),
        invokation(formulate(task, 4, X), X)
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
