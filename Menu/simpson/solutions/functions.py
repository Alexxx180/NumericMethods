from common.commander.formula import *
from common.drawing import Points
from menu.simpson.solutions.ends import Ends

def determine(b: float = None):
    task = Formula['Simpson'][0 if b is None else 1]
    return (
        lambda x: derive(task, x, 0),
        lambda x: derive(task, x, 4)
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
