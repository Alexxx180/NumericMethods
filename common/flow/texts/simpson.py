from common.drawing.table.table import Table
from common.commander.texts.fields import *
from common.handlers.interaction import pause
from common.handlers.printer import Printer

class Text:
    def __init__(self, name: str):
        self.fields = Fields[name]
        self.p = Printer(name).act(pause)

    def variables(self, model):
        self.p.keys('Model').args(model).print()

    def result(self, rows: list):
        fields = self.fields['Result']
        Table(fields).rows(rows).show()

    def pause(self):
        pause()
