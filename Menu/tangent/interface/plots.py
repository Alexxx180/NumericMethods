from numpy import linspace
from common.drawing.primitives.points import Points
from common.drawing.graphs.builder import CanvasBuilder
from common.drawing.graphs.spaces.scatter import ScatterSpace
from common.drawing.graphs.graphs import Graphs
from common.drawing.table.table import Table
from common.commander.texts.common import *
from common.commander.switch import View
from common.handlers.interaction import pause

class TangentPlots:
    def __init__(self, key: str, name: str, size: int, args: tuple, task):
        self.name = name
        self.length = size

        b = CanvasBuilder().space(ScatterSpace(name))
        b.graph(Graphs(1, 1)).formula(task)
        for space in (size, args):
            b.mark(space).plane()
        b.label(f'Plot {key}').entitle('Full Name')

        self.canvas = b.canvas

    def draw(row: list):
        for index, value in enumerate(row):
            x = float(value[0])
            y = float(value[1])

            half = self.length / 2
            points = linspace(x - half, x + half, self.length)
            tangent = float(num[2]) * (points - x) + y

            name = Texts[self.name]['Name'].format(index)
            order = (points, tangent, name, x, y)
            self.canvas.orders.append(order)

        self.canvas.show()
