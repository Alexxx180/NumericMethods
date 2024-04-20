from common.drawing import Graphs

class DefaultSpace:
    def __init__(graph: Graphs, color: str = 'red', names: tuple = ("График f(x)", "График f''''(x)")):
        self.single = []
        self.multi = []
        self.font = 12
        self.plot = graph
        self.ax = self.plot.ax[0]
        self.line = 'dashed'
        self.color = color
        self.align = ('left', 'bottom')
        self.names = names

    def append_text(x: float, count: int):
        relation = (self.points[0], x)
        for i in range(0, count):
            self.ax.text(x, self.points[i], f"{relation[i]:.2f}",
                fontsize=self.font, ha=self.align[0], va=self.align[1])

    def line(x: float, y: float):
        self.points = (y, 0)
        self.ax.vlines(x, self.points[1], self.points[0],
            colors=self.color, linestyles=self.line)

        for p in points:
            self.ax.plot(x, p, Drawing.Points[self.color])

        if abs(self.points[0]) > 0.01:
            append_text(x, len(self.points))

    def lines(values: tuple, f: callable):
        for x in values:
            line(x, f(x))

    def colored(color: str, values: tuple, f: callable):
        self.color = color
        lines(values, f)

    def show(self):
        for i in range(0, len(self.stones)):
            stone = self.stones[i]
            self.plot.based(stone[0].name, stone[0].base, i)
            self.plot.apply(stone[1], i)
        render()
        return self

    def render(self):
        for s in self.orders:
            if (len(s) == 3):
                self.color = s[2]
            if isinstance(s[0], tuple):
                lines(s[0], s[1])
            else:
                line(s[0], s[1])
