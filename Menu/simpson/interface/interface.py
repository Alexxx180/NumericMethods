from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from menu.simpson.solutions.functions import determine, search_max
from menu.simpson.solutions.solutions import SimpsonSolutions
from menu.simpson.interface.view import canvas, variables, output

class SimpsonInterface:
    def __init__(self, args: tuple):
        self.range = Ends(args)
        self.ends = Ends((args[2], args[3]))
        self.e = args[4]
        self.solution = SimpsonSolutions(self.ends)
        self.derives = determine(self.range.end)
        self.canvas = canvas(self.ends, self.derives)

    def calculate():
        d = { 0: self.derives[0], 4: self.derives[1] }

        ends: tuple = self.ends.margin()
        result = search_max(Points(ends, d[4]))
        self.solutions.core.resize(self.e, result[1])

        reorder(self.canvas.space, ends, result[0], d[0])
        return self.solutions.perform(self)

    def start():
        self.result = calculate(task)
        variables(self)
        output(self)
        self.canvas.show()
