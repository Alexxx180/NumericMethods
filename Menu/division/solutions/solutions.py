from numpy import arange
from common.commander.formula.formula import *
from common.calculus.objects.ends import Ends
from common.calculus.trigonometry import formulate
from common.drawing.graphs.spaces.plain import PlainSpace
from common.drawing.graphs.builder import CanvasBuilder
from common.drawing.graphs.graphs import Graphs
from menu.division.solutions.segment import Segment
from menu.division.solutions.functions import change_sequence

class SegmentDivision:
    def __init__(self, args: tuple):
        self.roots = []
        self.range = Ends(args[0], args[1])
        self.n = args[2]
        self.e = args[3]
        name = 'Division'

        derive = formulate(Formula[name], 0)
        self.formula = lambda x: derive(x)

        size = 100
        b = CanvasBuilder().space(PlainSpace(name))
        b.graph(Graphs(1, 1)).formula(self.formula)
        for space in ((-size, size), args):
            b.mark(space).plane()
        b.label('Plot')

        self.canvas = b.canvas
        self.segments = (Segment(0, 0), Segment(0, 0))

    def resign(self, interval: list) -> str:
        if self.segments[1].differs(self.segments[0]):
            self.roots.append(interval)
            return 'blue'
        return 'red'

    def study(self) -> list:
        self.segments[0].update(self.range.start, self.formula)
        step: float = self.range.size() / self.n

        for no in arange(1, self.n + 1, 1):
            interval: list = [x for x in self.segments]
            initial: float = self.range.start + step * no 
            self.segments[1].update(initial, self.formula)
            self.segments[0].set(self.segments[1])
            color: str = self.resign(interval)
            x: float = self.segments[0].x
            self.canvas.orders.append(
                (x, self.formula(x), color)
            )

        return self.roots

    def breakdown(self, x: tuple) -> tuple:
        while (x[1] - x[0]) > 2 * self.e:
            sequence(change_sequence, x)
        sequence(lambda x: x, x)

    def sequence(self, change: callable, x: tuple):
        self.space.lines(x) ; change(x) ; print(x)
