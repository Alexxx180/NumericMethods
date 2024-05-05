from common.drawing.table.table import Table
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from common.commander.resources import Resources

class Text:
    def __init__(self, name: str):
        self.fields: dict = Resources.Fields[name]
        self.p = Printer(name).act(pause)

    def variables(self, model):
        self.p.keys('Model').args(model).print()

    def result(self, rows: list):
        fields = self.fields['Result'].copy()
        Table(fields).rows(rows).show()

    def pause(self):
        pause()
