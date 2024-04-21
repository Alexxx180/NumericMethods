import matplotlib.pyplot as plt

class Graphs:
    def __init__(self, rows, cols):
        self.fig, self.ax = plt.subplots(rows, cols)
        self.color = 'black'
        self.width = 1.5
        self.basis = 0

    def __set(self, ax, x, y, title: str = ""):
        if title != "":
            ax.set_title(title)
        for axis in ('x', 'y'):
            c: Outline = locals()[axis]
            getattr(ax, f'set_{axis}lim')(c.min, c.max)
            getattr(ax, f'set_{axis}label')(axis)
        for d in ('h', 'v'):
            getattr(ax, f'ax{d}line')(self.basis,
                color=self.color, linewidth=self.width)
        ax.grid()
        return self

    def create(self, x, y, title: str = "", i: int = -1):
        return __set(self.ax if i == -1 else self.ax[i], x, y, title)

    def based(self, points, title: str = "", i: int = -1):
        x = Outline(points[0])
        y = Outline(points[1])
        return create(x, y, title, i)

    def build(self, x: list, y: list, i: int = -1):
        (self.ax if i == -1 else self.ax[i]).plot(x, y)
        return self

    def apply(self, points, i: int = -1):
        return build(points.X, points.Y, i)

    @staticmethod
    def show():
        plt.show()
