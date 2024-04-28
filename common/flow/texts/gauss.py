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
        self.p.act(print).keys('Solutions', 'Common').args(row).add()
        self.p.edit(1, name).args().add()
        return self.interrupt

    def zeros(self):
        self.p.act(print).keys('Solutions', 'Endless').args().add()
        return self.interrupt

    def process(self): self.p.act(pause).keys('Input', 'Data').args().add()

    def single(self): self.p.act(pause).keys('Input', 'Count').args().add()

    def varying(self): self.p.act(pause).keys('Input', 'Single').args().add()

    def no_solutions(self): self.p.act(print).keys('Solutions', 'Not found').args().add()

    def description(self): return self.p.keys('Input', 'String').text()

    def reverse_step(self, *args): self.p.act(print).keys('Reverse', 'Step').args(args).add()

    def reverse_course(self): self.p.act(print).keys('Reverse', 'Course').args().add()

    def straight_step(self, *args): self.p.act(print).keys('Straight', 'Step').args(args).add()

    def straight_course(self): self.p.act(print).keys('Straight', 'Course').args().add()

    def source(self, array):
        fields = Fields[self.name, 'Source']
        Table(fields).matrix(array).show()

    def result(self, result):
        Table().matrix(result).floats('.3').show()
