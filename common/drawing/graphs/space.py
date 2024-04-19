from common.drawing import Graphs

class DefaultSpace:
    def __init__(graph: Graphs, color: str = 'red'):
        self.font = 12
        self.plot = graph
        self.line = 'dashed'
        self.color = color
        self.align = ('left', 'bottom')
        self.names = ("График f(x)", "График f''''(x)")

    def append_text(x: float, count: int):
        relation = (self.points[0], x)
        for i in range(0, count):
            self.plot.ax.text(x, self.points[i], f"{relation[i]:.2f}",
                fontsize=self.font, ha=self.align[0], va=self.align[1])

    def line(x: float, y: float):
        self.points = (y, 0)
        self.plot.ax.vlines(x, self.points[1], self.points[0],
            colors=self.color, linestyles=self.line)

        for p in points:
            self.plot.ax.plot(x, p, Drawing.Points[self.color])

        if abs(self.points[0]) > 0.01:
            append_text(x, len(self.points))

    def lines(values: tuple, f: callable):
        for x in values:
            line(x, f(x))

    def colored(color: str, values: tuple, f: callable):
        self.color = color
        lines(values, f)

    def show(stone: Milestone):
        self.plot.based(stone.name, stone.overlay)
        self.plot.apply(stone.base).apply(stone.overlay).show()
        return self
