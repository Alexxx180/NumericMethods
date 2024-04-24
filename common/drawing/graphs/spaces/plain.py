from common.drawing.drawing import *

class PlainSpace:
    def __init__(self, name: str, color = 'red'):
        self.name = name
        self.color = color
        self.fontsize = 12
        self.line = 'dashed'
        self.align = {
            'horizontal': 'left',
            'vertical': 'bottom'
        }

    def set_graph(self, graph, i: int = -1):
        self.plot = graph
        self.ax = self.plot.ax if i == -1 else self.plot.ax[i]

    def append_text(self, x: float, count: int):
        relation = (self.points[0], x)
        for i in range(0, count):
            self.ax.text(x, self.points[i], f"{relation[i]:.2f}", fontsize=self.fontsize, ha=self.align['horizontal'], va=self.align['vertical'])

    def line(self, x: float, y: float):
        self.points = (y, 0)
        self.ax.vlines(x, self.points[1], self.points[0],
            colors=self.color, linestyles=self.line)

        for p in points:
            self.ax.plot(x, p, Points[self.color])

        if abs(self.points[0]) > 0.01:
            append_text(x, len(self.points))

    def lines(self, values: tuple, f: callable):
        for x in values:
            self.line(x, f(x))

    def show(self):
        pass

    def render(self, order):
        basis = order[0] ; drawing = order[1]
        if (len(order) == 3):
            self.color = order[2]
        if isinstance(basis, tuple):
            self.lines(basis, drawing)
        else:
            self.line(basis, drawing)
