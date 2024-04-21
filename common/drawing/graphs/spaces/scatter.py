from common.commander.texts.common import *

class ScatterSpace:
    def __init__(graph, name: str, color: str = 'red'):
        self.orders = []
        self.plot = graph
        self.name = name
        self.color = color

    def set_graph(graph, i: int = -1):
        self.plot = graph
        self.ax = self.plot.ax if i == -1 else self.plot.ax[i]

    def draw(basis: list, line: float, label: str):
        self.plot.ax.plot(basis, line, label=label, linestyle='--')

    def scatters(x: float, y: float):
        self.plot.ax.scatter(x, y, color=self.color,
            label=Texts[self.name]['Point'])

    def show():
        self.plot.ax.legend()

    def render(self, order: tuple):
        draw(order[0], order[1], order[2])
        scatters(order[4], order[5])
