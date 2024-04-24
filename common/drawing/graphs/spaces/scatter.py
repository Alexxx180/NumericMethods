from common.commander.texts.common import *

class ScatterSpace:
    def __init__(self, name: str, color: str = 'red'):
        self.name = name
        self.color = color

    def set_graph(self, graph, i: int = -1):
        self.plot = graph
        self.ax = self.plot.ax if i == -1 else self.plot.ax[i]

    def draw(self, basis: list, line: float, label: str):
        self.plot.ax.plot(basis, line, label=label, linestyle='--')

    def scatters(self, x, y):
        self.plot.ax.scatter(x, y, color=self.color,
            label=Texts[self.name]['Point'])

    def show(self):
        self.plot.ax.legend()

    def render(self, order: tuple):
        self.draw(order[0], order[1], order[2])
        self.scatters(order[4], order[5])