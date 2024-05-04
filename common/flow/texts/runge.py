from common.drawing.table.table import Table
from common.commander.texts.fields import *

class Text:
    def __init__(self, name: str, key: str):
        self.fields = Fields[name]
        self.key = key

    def source(self, values: tuple):
        print(len(values), values)
        Table(self.fields[self.key]['Source']).row(values).show()
        return self

    def result(self, values: list, formula: str = ''):
        fields = self.fields[self.key]['Result'].copy()
        if formula != '':
            fields[0] += f': {formula}'
            fields[6] = formula
        Table(fields).columns(0, values).floats('.8').show().pause()
