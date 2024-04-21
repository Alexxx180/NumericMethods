from numpy import linspace
from common.drawing import Points, Graphs, Table
from common.commander.texts.common import *
from common.commander.Commander import View
from menu.handlers.func import pause

class TangentPlots:
    def __init__(self, name: str, size: int, args: tuple, task):
        self.name = name
        self.length = size

        b = CanvasBuilder(name)
        b.space(ScatterSpace()).graph(Graphs(1, 1)).formula(task)
        b.mark(size).plane().mark(args).plane().label(f'Plot {key}')

        self.canvas = b.canvas

    def draw(row: list):
        for index, num in enumerate(row):
            x = float(num[0])
            y = float(num[1])

            half = self.length / 2
            points = linspace(x - half, x + half, self.length)
            tangent = float(num[2]) * (points - x) + y

            name = Texts[self.name]['Name'].format(index)
            order = (points, tangent, name, x, y)
            self.canvas.orders.append(order)

        self.canvas.show()
