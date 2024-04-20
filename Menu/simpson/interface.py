from common.drawing import Points
from common.calculation.objects import Ends
from common.calculation.trigonometry import derive
from menu.solutions.functions import determine, search_max
from menu.solutions.solutions import SimpsonSolutions
from menu.interface.view import space, variables, output, view

class SimpsonInterface:
    def __init__(self, args: tuple):
        self.range = Ends(args)
        self.ends = Ends((args[2], args[3]))
        self.e = args[4]
        self.solution = SimpsonSolutions(self.ends)
        self.space = space(self.ends.margin(0.5))
        self.derives = determine(self.range.end)

    def calculate():
        d = { 0: self.derives[0], 4: self.derives[1] }

        ends: tuple = self.ends.margin()
        result = search_max(Points(ends, d[4]))
        self.solutions.core.resize(self.e, result[1])

        reorder(self.space, ends, result[0], d[0])
        overlay(self.space, self.ends.margin(10), self.derives)
        return self.solutions.perform(self)

    def start():
        self.result = calculate(task)
        variables(self)
        output(self)
        view(self)
