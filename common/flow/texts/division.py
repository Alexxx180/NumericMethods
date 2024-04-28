from common.handlers.printer import Printer
from common.handlers.interaction import pause

class Text:
    def __init__(self, name: str):
        self.name = name
        self.p = Printer(name).act(print)
        self.rows = []

    def research(self, formula, initial):
        self.p.keys('Formula').args(formula).add()
        self.p.keys('Research').args(initial).add()

    def interval(self, *args):
        self.p.keys('Interval').args(args).add()

    def no_roots(self):
        self.p.keys('No roots').args().add().print().clear()

    def roots(self, result):
        self.p.keys('Roots').args(result).add().print().clear()

    def source(self, roots):
        grid(self.name, 'Source').row(roots).show()

    def result(self):
        grid(self.name, 'Result').row(self.rows).show()
        return self

    def pause(self):
        pause()
