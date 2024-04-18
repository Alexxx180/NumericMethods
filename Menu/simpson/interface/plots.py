class SimpsonPlots:
    def __init__(ab: tuple):
        self.font = 12
        self.plot = Graphs(1, 2)
        self.color = 'red'
        self.align = ('left', 'bottom')
        self.names = ("График f(x)", "График f''''(x)")

        task = formula(ab).tasks[0 if b is None else 1]

        self.derives = (lambda x: derive(task, x, 0),
            lambda x: derive(task, x, 4))

    def create_plots():
        for i in range(len(self.names)):
            self.plot.createas(self.names[i], self.points, i)

        for i in range(len(self.derives)):
            self.plot.based(Points(self.xy, self.derives[i]), "", i)

    def append_text(x, points: tuple):
        relation = (points[0], x)
        for i in range(0, len(relation)):
            self.plot.ax.text(x, points[i], f"{relation[i]:.2f}",
                fontsize=font, ha=self.align[0], va=self.align[1])

    def line(x: float, y: float):
        points = (y, 0)
        self.plot.ax.vlines(x, points[1], y,
            colors=self.color, linestyles='dashed')

        for p in points:
            self.plot.ax.plot(x, p, Drawing.Points[self.color])

        if abs(y) > 0.01:
            append_text(x, points)

    def lines(values: tuple, f: callable):
        for x in values:
            line(x, f(x))
