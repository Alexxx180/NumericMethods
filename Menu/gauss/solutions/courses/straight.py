from numpy import column_stack, ndarray
from common.drawing.table.table import Table

"""
Python slice syntax

https://stackoverflow.com/questions/509211/how-slicing-in-python-works
"""

index: int = 0
result = None

def step(text, k: int, a, b: list):
    global result, index
    start: int = k + 1
    end: int = a.shape[0]

    for i in range(start, end):
        index += 1
        text.straight_step(index, i + 1, start, a[i, k], a[k, k])

        ratio = a[i, k] / a[k, k]
        a[i, k:] -= ratio * a[k, k:]
        b[i] -= ratio * b[k]

        result = column_stack((a, b))
        text.result(result)

def straight(text, n: int, a, b: list):
    global result, index
    text.straight_course()
    index = 0

    for k in range(n):
        step(text, k, a, b)

    return result
