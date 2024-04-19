from common.calculation.objects.end import Ends
from common.drawing.graphs.space import DefaultSpace
from common.drawing.graphs.milestone import Milestone
from menu.division.solutions.segment import Segment
from menu.division.solutions.functions import change_sequence

class SegmentDivision:
    def __init__(self, args: tuple):
        self.roots = []
        self.range = Ends(args)
        self.n = args[2]
        self.e = args[3]
        self.formula = Formula['Division']
        self.stone = Milestone('График А', args)
        self.space = DefaultSpace(Graphs(1, 1), 'blue')
        self.segments = (Segment(0, 0), Segment(0, 0))

    def show():
        self.space.show(self.stone)
        return self

    def resign(self, interval: list) -> str:
        if self.current.differs(self.previous):
            self.roots.append(interval)
            return 'blue'
        return 'red'

    def study(self) -> list:
        self.segments[0].update(a)
        step: float = self.range.size() / self.n

        for no in arange(1, self.n + 1, 1):
            interval: list = [x for x in self.segments]
            self.segments[1].update(self.range.start + step * no)
            self.segments[0].set(self.current)
            self.space.colored(resign(interval), interval, self.formula)

        return self.roots

    def breakdown(self, x: tuple) -> tuple:
        while (x[1] - x[0]) > 2 * self.e:
            sequence(change_sequence, x)
        sequence(lambda x: x, x)

    def sequence(self, change: callable, x: tuple):
        self.space.lines(x) ; change(x) ; print(x)
