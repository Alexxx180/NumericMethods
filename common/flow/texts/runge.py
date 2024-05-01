from common.drawing.table.table import Table
from common.commander.texts.fields import *

class Text:
    def __init__(self, name: str, key: str):
        self.fields = Fields[name]
        self.key = key

    def source(self, values: list):
        Table(self.fields[self.key]['Source']).row(values).show()
        return self

    def result(self, values: list, i: int = -1):
        fields = self.fields[self.key]['Result']
        if i != -1:
            fields[0] += str(i + 1)
            fields[7] = self.fields['Functions'][i]
        Table(fields).columns(0, values).show().pause()
