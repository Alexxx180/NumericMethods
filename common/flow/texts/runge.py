from common.drawing.table.table import Table
from common.commander.texts.fields import *

class Text:
    def __init__(self, name: str):
        self.name = name

    def source(self, key: str, values: list):
        fields = Fields[self.name][key]['Source']
        Table(fields).row(values).show()

    def result(self, key: str, values: list, i: int = -1):
        fields = Fields[self.name][key]['Result']
        if i != -1:
            fields[0] += str(i + 1)
            fields[7] = Fields[self.name]['Functions'][i]
        Table(fields).columns(0, values).show().pause()
