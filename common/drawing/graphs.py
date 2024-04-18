import matplotlib.pyplot as plt

class Graphs:
    def __init__(self, rows, cols):
        self.fig, self.ax = plt.subplots(rows, cols)
        self.labels = ('x', 'y')
        self.color = 'black'
        self.width = 1.5
        self.basis = 0

    def __set(self, ax, color: str, width: float, x_min: int, x_max: int, y_min: int, y_max: int, title: str = ""):
        if title != "":
            ax.set_title(title)
        ax.set_xlabel(self.labels[0])
        ax.set_ylabel(self.labels[1])
        for line in (ax.axhline, ax.axvline):
            line(self.basis, color=self.color, linewidth=self.width)
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
        ax.grid()

    def create(self, x_min: int, x_max: int, y_min: int, y_max: int, title: str = "", i: int = -1):
        __set(self.ax if i == -1 else self.ax[i], x_min, x_max, y_min, y_max, title)
        return self

    def createas(self, points: tuple, title: str = "", i: int = -1):
        return create(points[0], points[1], points[2], points[3], title, i)

    def points(self, x: list, y: list, title: str = "", i: int = -1):
        return create(min(x), max(x), min(y), max(y), title, i)

    def based(self, points, title: str = "", i: int = -1):
        return points(title, points.X, points.Y, i)

    def build(self, x: list, y: list, i: int = -1):
        ax = self.ax if i == -1 else self.ax[i]
        ax.plot(x, y)
        return self

    def apply(self, points, i: int = -1):
        return build(points.X, points.Y, i)

    @staticmethod
    def show():
        plt.show()
