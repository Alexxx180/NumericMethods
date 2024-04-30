from common.drawing.table.table import Table
from common.commander.texts.fields import *
from common.handlers.interaction import pause
from common.handlers.printer import Printer

class Text:
    def __init__(self, name: str):
        self.name = name
        self.p = Printer(name)

    def message(self, text: str):
        self.p.act(print).keys('Message').args(text).print()

    def no_roots(self, a: float, b: float):
        self.p.act(pause).keys('No roots').args(a, b).print()

    def formula(self, rows: list):
        fields = Fields[self.name]['Formula']
        Table(fields).rows(rows).align('Left', 'Уравнение').show().pause()

    def result(self, rows: list):
        fields = Fields[self.name]['Result']
        Table(fields).rows(rows).show().pause()

    def pause(self):
        pause()
