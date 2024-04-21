from numpy import linspace
from common.drawing import Points, Graphs, Table
from common.commander.texts.common import *
from common.commander.Commander import View
from menu.handlers.func import pause

class TangentInterface:
    def __init__(self, name: str, size: int):
        self.name = name
        self.length = 100
        self.plot = Graphs(1, 1)
        self.base = Points((-size, size), task)
        self.overlay = Points(abe, task)

    def output(row: list):
        self.plot.ax.legend()
        Table(Tangent['Result'], self.message).row(row).show().pause()

    def draw_graph(basis: float, line: float, x: float, y: float, index: int):

        self.plot.ax.plot(basis, line, label=Texts['Name'].format(index), linestyle='--')
        self.plot.ax.scatter(x, y, color='red', label=Texts['Point'])

    def memorize(message: str):
        self.message = message
        print(Texts['Message'].format(message))

    def no_roots(a: float, b: float):

    def draw_tangent(row: list):
        for index, num in enumerate(row):
            x = float(num[0]); y = float(num[1])

            half = self.length / 2
            points = linspace(x - half, x + half, self.length)
            tangent = float(num[2]) * (points - x) + y

            draw_graph(points, tangent, x, y, index)
        output(row)

    def show_graph():
        self.plot.based(self.overlay, Texts['Plot'].format(self.name))
        self.plot.apply(self.base).apply(self.overlay)
        if View('Plot', 'Tangent'):
            self.plot.show()
