from sympy.abc import x, a, b
from common.commander.resources import Resources
from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from common.calculus.trigonometry import formulate, invokation, express
from common.drawing.drawing import *

def empty_list() -> list: return [Chars['None'] * 2]

def placeholder(x0: float) -> list:
    row = empty_list()
    row.insert(1, Chars['Miss'])
    row.insert(0, x0)
    return row

def __form(text: str, *args) -> tuple:
    return (text, formulate(text, 4, *args))

def determine(text, a: float, b: float, form: str) -> dict:
    task = Resources.Formula['Simpson'][form]
    real = __form(task.format(a=a, b=b), x)
    text.formula(real[0], str(real[1]))
    return {
        1: invokation(express(real[0]), x),
        4: invokation(real[1], x)
    }

def search_max(points) -> tuple:
    maxed = max(map(abs, points.Y))
    pts = enumerate(points.Y)

    indices = [i for i, value in pts if abs(value) == maxed]
    index = int(indices[0])
    return { 'm': maxed, 'x': points.X[index] }

def quadratic(size: float, m: float, e: float) -> int:
    n = (m * (size ** 5) / (180 * e)) ** 0.25

    if not isinstance(n, int): n = int(n + 1)

    while n % 2 != 0: n += 1

    return n
