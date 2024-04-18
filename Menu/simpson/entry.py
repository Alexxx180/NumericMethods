from Simpson_formula.Functions import s_f, define_n, define_m, func
from Classes.Graphs import Graphs
from Classes.Points import PointGraphs
from hendllers.func import pause
import common.commander
from Classes.Input import UserSelect
from common.calc.TrigonometryFunctions import derive

class SimpsonMethod:
    def __init__(ab: tuple):
        self.ab = ab
        self.plot = Graphs(1,2)
        self.root = (0.0, 0)
        self.names = ("График f(x)", "График f''''(x)")

        task = formula(ab).tasks[0 if ab[1] is None else 1]

        self.derives = (lambda x: derive(task, x, 0),
            lambda x: derive(task, x, 4))

    def Calculate(ends: Ends, precision: float):
        self.root[0]: float = search_max(ends, self.derives[1], plot.ax[1])
        self.root[1]: int = quadratic(ends.size(), maximum, precision)

        self.xy: tuple = ends.margin(10)

        return perform(ends, root, derives[1], plot.ax[0])

    def Simpson(ends: Ends, precision: float):
        size = 10
        offset = ends.margin(0.5)
        self.points = (offset[0], offset[1], -size, size)

        result = Calculate(ends, precision, task)

        SegmentPrint.integration(ab, ends, precision, self.root, result)
        if Commander.Plots['Simpson'] or UserSelect(""):
            self.plot.show()
