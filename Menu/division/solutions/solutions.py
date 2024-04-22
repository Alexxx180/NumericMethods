from common.calculus.objects.ends import Ends
from common.drawing.graphs.spaces.scatter import ScatterSpace
from common.drawing.graphs.builder import CanvasBuilder
from common.drawing.graphs.graphs import Graphs
from menu.division.solutions.segment import Segment
from menu.division.solutions.functions import change_sequence

class SegmentDivision:
    def __init__(self, args: tuple):
        self.roots = []
        self.range = Ends(args)
        self.n = args[2]
        self.e = args[3]
        name = 'Division'
        self.formula = Formula[name]

        b = CanvasBuilder(name)
        b.space(ScatterSpace()).graph(Graphs(1, 1)).formula(task)
        b.mark(size).plane().mark(args).plane().label(f'Plot')

        self.canvas = b.canvas
        self.segments = (Segment(0, 0), Segment(0, 0))

    def resign(self, interval: list) -> str:
        if self.current.differs(self.previous):
            self.roots.append(interval)
            return 'blue'
        return 'red'

    def study(self) -> list:
        self.segments[0].update(self.range.start)
        step: float = self.range.size() / self.n

        for no in arange(1, self.n + 1, 1):
            interval: list = [x for x in self.segments]
            self.segments[1].update(self.range.start + step * no)
            self.segments[0].set(self.current)
            color: str = resign(interval)
            self.canvas.orders.append((interval, self.formula, color))

        return self.roots

    def breakdown(self, x: tuple) -> tuple:
        while (x[1] - x[0]) > 2 * self.e:
            sequence(change_sequence, x)
        sequence(lambda x: x, x)

    def sequence(self, change: callable, x: tuple):
        self.space.lines(x) ; change(x) ; print(x)
