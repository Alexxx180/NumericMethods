import matplotlib.pyplot as plt
from common.drawing.primitives.outline import Outline

class Graphs:
    def __init__(self, rows, cols):
        self.fig, self.ax = plt.subplots(rows, cols)
        self.color = 'black'
        self.width = 1.5
        self.basis = 0

    def __set(self, ax, x, y, title: str = ""):
        if title != "":
            ax.set_title(title)
        ax.set_xlim(x.min, x.max)
        ax.set_ylim(y.min, y.max)
        for axis in ('x', 'y'):
            #c: Outline = locals()[axis]
            #print(c.min, c.max)
            #getattr(ax, f'set_{axis}lim')(c.min, c.max)
            getattr(ax, f'set_{axis}label')(axis)
        for d in ('h', 'v'):
            getattr(ax, f'ax{d}line')(self.basis,
                color=self.color, linewidth=self.width)
        ax.grid()
        return self

    def create(self, x, y, title: str = "", i: int = -1):
        ax = self.ax if i == -1 else self.ax[i]
        return self.__set(ax, x, y, title)

    def based(self, points, title: str = "", i: int = -1):
        x = Outline(points.X)
        y = Outline(points.Y)
        #print(f"Problem {points[0]}, {points[1]}")
        return self.create(x, y, title, i)

    def build(self, x: list, y: list, i: int = -1):
        (self.ax if i == -1 else self.ax[i]).plot(x, y)
        return self

    def apply(self, points, i: int = -1):
        return self.build(points.X, points.Y, i)

    @staticmethod
    def show():
        plt.show()
