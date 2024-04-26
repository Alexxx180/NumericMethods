from common.drawing.drawing import *
from menu.simpson.solutions.core import SimpsonCore

class SimpsonSolutions:
    def __init__(self, ends, f: callable):
        self.core = SimpsonCore(ends, f)
        self.rows = []

    @staticmethod
    def __empty_list():
        return [Chars['None'] * 2]

    def blanks(self, row: list):
        row.extend(__empty__list())
        self.rows.append(row)

    def values(self):
        row = __empty_list()
        row.insert(1, Chars['Miss'])
        row.insert(0, self.core.x)
        row[len(row) - self.core.i] = self.core.y
        self.rows.append(row)

    def perform(self, view):
        core = self.core
        view.origins(core)
        blanks([core.start, core.yends.start])

        for i in range(1, n):
            self.core.iteration(i)
            values(core)
            view.space.orders.append(core.coords())

        blanks([core.end, core.yends.end])
        view.output(core.n)
        return core.calculate()
