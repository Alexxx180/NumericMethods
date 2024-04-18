from numpy import arrange
import menu.division.interface.plots
import menu.division.interface.print
import menu.division.solutions.segment

class SegmentDivision:
    def __init__(self, ax):
        self.roots = []
        self.plots = SegmentPlots("blue", ax)
        self.previous = Segment(0, 0)
        self.current = Segment(0, 0)

    def sign_change(self, interval: tuple) -> str:
        if self.current.differs(self.previous):
            self.roots.append(interval)
            return "blue"
        return "red"

    def study(self, a: float, b: float, n: int) -> list:
        SegmentPrint.start(a, b)
        self.previous.update(a)

        step: float = (b - a) / n

        for no in arange(1, n + 1, 1):
            interval: tuple = (self.previous.x, self.current.x)

            self.current.update(a + step * no)
            self.plots.color = sign_change(interval)
            self.plots.lines(interval)
            self.previous.set(self.current)

        return self.roots

    def breakdown(self, x: tuple, e: float) -> tuple:
        self.plots.color: str = "green"

        while (x[1] - x[0]) > 2 * e:
            self.plots.sequence(change_sequence, x)
        self.plots.sequence(lambda x: x, x)
