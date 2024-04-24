from numpy import column_stack, ndarray
from common.drawing.table.table import Table
from common.commander.texts.common import *

"""
Python slice syntax

https://stackoverflow.com/questions/509211/how-slicing-in-python-works
"""

index: int = 0
result = None

def step(k: int, a, b: list):
    global result, index
    text = Texts['Gauss']['Straight']['Step']

    start: int = k + 1
    end: int = a.shape[0]

    for i in range(start, end):
        index += 1
        print(text.format(index, i + 1, start, a[i][k], a[k, k]))

        ratio = a[i, k] / a[k, k]
        a[i, k:] -= ratio * a[k, k:]
        b[i] -= ratio * b[k]

        result = column_stack((a, b))

        Table().matrix(result).floats('.3').show()

def straight(n: int, a, b: list):
    global result, index
    print(Texts['Gauss']['Straight']['Course'])
    index = 0

    for k in range(n):
        step(k, a, b)

    return result