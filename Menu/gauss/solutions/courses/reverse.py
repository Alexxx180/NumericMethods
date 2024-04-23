from numpy import zeros, dot
from common.drawing.table import Table
from common.commander.texts.common import *

def step(x: list, i: int, a: list, b: list):
    start: int = i + 1

    scalar = dot(a[i, start:], x[start:])
    x[i] = (b[i] - scalar) / a[i, i]

    print(Texts['Gauss']['Reverse']['Step'].format(start, x[i]))


def reverse(n: int, a, b: list):
    print(Texts['Gauss']['Reverse']['Course'])
    x = zeros(n)

    start: int = a.shape[0] - 1

    for i in range(start, -1, -1):
        step(x, i, a, b)
