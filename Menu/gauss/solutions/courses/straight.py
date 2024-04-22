from numpy import column_stack
from common.drawing.table import Table
from common.commander.texts.common import *

"""
Python slice syntax

https://stackoverflow.com/questions/509211/how-slicing-in-python-works
"""

def step(k: int, a, b: list, index: int):
    text = Texts['Straight']['Step']

    start: int = k + 1
    end: int = a.shape[0]

    for i in range(start, end):
        index += 1
        print(text.format(index, i + 1, start, a[i][k], a[k, k]))

        ratio = a[i, k] / a[k, k]
        a[i, k:] -= ratio * a[k, k:]
        b[i] -= ratio * b[k]

        columns = column_stack((a, b))
        Table().matrix(columns).show()

    return columns

def straight(n: int, a, b: list):
    print(Texts['Straight']['Course'])
    index = 0

    for k in range(n):
        result = step(k, a, b, index)

    return result
