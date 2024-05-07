from common.commander.switch import View
from common.drawing.primitives.points import Points
from common.calculus.objects.ends import Ends
from menu.simpson.solutions.functions import determine, search_max
from menu.simpson.solutions.solutions import SimpsonSolutions
from common.flow.texts.simpson import Text
from common.flow.canvas.simpson import canvas_from

class SimpsonInterface:
    def __init__(self, args: tuple, name: str, form: str):
        self.name: str = name
        self.text = Text(name)

        self.range = Ends(args)
        self.ends = Ends((args[2], args[3]))
        self.e: float = args[4]

        self.derives = determine(args[0], args[1], form)
        self.solution = SimpsonSolutions(self.ends, self.derives[1])

        self.canvas = canvas_from(name, self.ends, self.derives)
        self.orders: list = []

    def calculate(self):
        ends: tuple = self.ends.margin()
        f: callable = self.derives[4]
        result = search_max(Points(ends, f))
        self.solution.core.resize(self.e, result['m'])

        x: float = result['x']
        self.orders.append(1)
        self.orders.append((x, f(x)))
        self.orders.append(0)
        self.orders.append((ends, self.derives[1]))

        return self.solution.perform(self)

    def start(self):
        self.result = self.calculate()
        self.text.variables(self)

        if self.solution.core.n <= 15 or View('Table', self.name):
            self.text.result(self.solution.rows)

        self.canvas.show(self.orders)
        self.text.pause()
