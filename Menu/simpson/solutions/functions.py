from common.commander.formula.formula import *
from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from common.calculus.trigonometry import formulate, invokation

def determine(ab, form: str):
    if ab.end is None:
        task = Formula['Simpson'][form](ab.start)
    else:
        task = Formula['Simpson'][form](ab.start, ab.end)
    return (
        invokation(formulate(task, 0)),
        invokation(formulate(task, 4))
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
