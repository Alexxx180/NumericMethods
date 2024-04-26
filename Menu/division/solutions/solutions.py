from numpy import arange
from common.calculus.objects.ends import Ends
from menu.division.solutions.segment import Segment
from menu.division.solutions.functions import swap, resign

class SegmentDivision:
    def __init__(self, args: tuple, derive: callable):
        self.roots = []
        self.orders = []
        self.range = Ends(args)
        self.precision = Ends(args[2], args[3])
        self.formula = derive
        part = Segment(0, 0)
        self.segments = (part, part.copy())

    def study(self) -> list:
        n: int = self.precision.start
        a: float = self.range.start

        self.segments[0].update(a, self.formula)
        step: float = self.range.size() / n

        for no in arange(1, n + 1, 1):
            interval: list = [x for x in self.segments]
            initial: float = a + step * no 

            self.segments[1].update(initial, self.formula)
            self.segments[0].set(self.segments[1])

            color: str = resign(self.roots, self.segments, interval)
            x: float = self.segments[0].x
            order: tuple = (x, self.formula(x), color)

            self.orders.append(order)

    def breakdown(self, x: tuple) -> tuple:
        e: float = self.precision.end
        while (x[1] - x[0]) > 2 * e:
            self.orders.append(sequence(swap, x, self.formula))
        self.orders.append(sequence(lambda x: x, x, self.formula))
