from menu.simpson.solutions.core import SimpsonCore
from menu.simpson.solutions.functions import empty_list, placeholder

class SimpsonSolutions:
    def __init__(self, ends, f: callable):
        self.core = SimpsonCore(ends, f)
        self.rows = []

    def blanks(self, row: list):
        row.extend(empty_list())
        self.rows.append(row)

    def values(self):
        row = placeholder(self.core.x)
        i: int = len(row) - self.core.i - 1
        row[i] = self.core.y
        self.rows.append(row)

    def perform(self, view):
        x = self.core.ends
        y = self.core.yends
        self.blanks([x.start, y.start])

        for i in range(1, self.core.n):
            self.core.iteration(i)
            coords = self.core.coords()
            self.values()
            view.orders.append(coords)

        self.blanks([x.end, y.end])
        return self.core.calculate()
