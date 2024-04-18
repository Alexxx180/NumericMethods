import Classes.drawing
from menu.division.solutions.functions import formula

class SegmentPlots:
    def __init__(self, color: str, ax):
        self.color = color
        self.ax = ax

    def lines(self, values: tuple):
        line(x for x in values)

    def sequence(self, change: callable, x: tuple):
        lines(x)
        change(x)
        print(f"[{x[0]}, {x[1]}]")

    def append_text(x: float, points: tuple):
        previous = points[0]
        formats = (f"{previous:.2f}", f"{x:.2f}")

        if abs(previous) > 0.01:
            for i in range(0, len(points)):
                self.ax.text(x, points[i], formats[i], fontsize=12, ha='left', va='bottom')

    def line(x: float):
        points = (formula(x), 0)

        self.ax.vlines(x, points[1], points[0], colors=self.color, linestyles='dashed')
        for p in points:
            self.ax.plot(x, p, Drawing.Points['red'])
        append_text(x, points)
