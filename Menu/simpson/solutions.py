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

    def blanks(row: list):
        row.extend([Chars['None'], Chars['None']])
        self.rows.append(row)

    def values(x: float, i: int, y: float):
        row = [x, Chars['None'], Chars['Miss'], Chars['None']]
        row[len(row) - i] = y
        self.rows.append(row)

    def perform(ends: Ends, n: int, f: callable, view: SimpsonInterface):
        yends = Ends(f(ends.start), f(ends.end))
        h: float = ends.size() / n # H в методичке
        middle: float = yends.sub() / 2 # S в методичке
        result: float = yends.sum()
        view.out_h(h)
        view.lines(ends, f)

        blanks(rows, [ends.start, yends.start])

        for i in range(1, n):
            c: int = i % 2
            x: float = ends.start + i * h
            y: float = f(x)
            view.line(x, y)

            factor: int = 2
            result += (factor + factor * c) * y
            values(x, current, y)

        blanks(rows, [ends.end, yends.end])

    view.output(n)

    return h / 3 * result
