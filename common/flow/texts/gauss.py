from common.drawing.table.table import Table
from common.commander.texts.fields import *
from common.handlers.interaction import pause
from common.handlers.printer import Printer

class Text:
    def __init__(self, name: str):
        self.p = Printer(name)
        self.name = name
        self.interrupt = True

    def empty(self, name: str, row: list):
        self.p.act(print).keys('Solutions', 'Common').args(row).print()
        self.p.edit(1, name).args().print()
        return self.interrupt

    def zeros(self):
        self.p.act(print).keys('Solutions', 'Endless').args().print()
        return self.interrupt

    def process(self):
        self.p.act(pause).keys('Input', 'Data').args().print()

    def single(self):
        self.p.act(pause).keys('Input', 'Count').args().print()

    def varying(self):
        self.p.act(pause).keys('Input', 'Single').args().print()

    def no_solutions(self):
        self.p.act(print).keys('Solutions', 'Not found').args().print()

    def description(self): return self.p.keys('Input', 'String').text()

    def reverse_step(self, *args):
        self.p.act(print).keys('Reverse', 'Step').args(args).print()

    def reverse_course(self):
        self.p.act(print).keys('Reverse', 'Course').args().print()

    def straight_step(self, *args):
        self.p.act(print).keys('Straight', 'Step').args(*args).print()

    def straight_course(self):
        self.p.act(print).keys('Straight', 'Course').args().print()

    def source(self, array):
        fields = Fields[self.name]['Source']
        Table(fields).matrix(array).show()

    def result(self, result):
        Table().matrix(result).floats('.3').show()

    def pause(self):
        pause()
