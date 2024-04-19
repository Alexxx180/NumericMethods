import numpy as np
from Classes.Points import PointGraphs
from Classes.Table import Table
from Classes.Input import UserSelect
import common.drawing
from common.commander import View

from common.calc.TrigonometryFunctions import derive

class SimpsonFunctions:
    def __init__():
        self.rows = []

    def __empty_list():
        return [Chars['None'] * 2]

    def blanks(row: list):
        row.extend(__empty__list())
        self.rows.append(row)

    def values(x: float, i: int, y: float):
        row = __empty_list()
        row.insert(1, Chars['Miss'])
        row.insert(0, x)
        row[len(row) - i] = y
        self.rows.append(row)

    def perform(ends: Ends, n: int, f: callable, view: SimpsonInterface):
        yends = Ends(f(ends.start), f(ends.end))

        size: float = ends.size() / n # H в методичке
        middle: float = yends.sub() / 2 # S в методичке
        result: float = yends.sum()

        view.origins(size, ends, f)
        blanks(rows, [ends.start, yends.start])

        for i in range(1, n):
            factor: int = 2

            c: int = i % factor
            x: float = ends.start + i * size
            y: float = f(x)

            result += (factor + factor * c) * y

            values(x, c, y)
            view.line(x, y)

        blanks(rows, [ends.end, yends.end])

    view.output(n)

    return size / 3 * result
