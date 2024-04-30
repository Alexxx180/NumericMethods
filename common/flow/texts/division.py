from common.drawing.table.table import Table
from common.commander.texts.fields import *
from common.handlers.printer import Printer
from common.handlers.interaction import pause

class Text:
    def __init__(self, name: str):
        self.name = name
        self.p = Printer(name).act(print)
        self.rows = []

    def research(self, formula, initial):
        self.p.keys('Formula').args(formula).print()
        self.p.keys('Research').args(initial).print()

    def no_roots(self):
        self.p.keys('No roots').args().print()

    def roots(self, result):
        self.p.keys('Roots').args(result).print()

    def source(self, roots):
        fields = Fields[self.name]['Source']
        Table(fields).rows(roots).show()
        return self

    def result(self, *args):
        self.p.keys('Result').args(*args).print()

    def pause(self):
        pause()
