from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name)

    def message(self, text: str):
        self.p.act(print).keys('Message').args(text).print()

    def no_roots(self, a: float, b: float):
        self.p.act(pause).keys('No roots').args(a, b).print()

    def formula(self, rows: list):
        fields = self.fields['Formula'].copy()
        Table(fields).rows(rows).align('Left', 'Уравнение').show().pause()

    def result(self, rows: list):
        fields = self.fields['Result'].copy()
        Table(fields).rows(rows).show().pause()

    def pause(self, text: str = ''):
        pause(text)
