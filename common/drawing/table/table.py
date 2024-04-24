from common.handlers.interaction import pause
from common.drawing.table.struct import TableStruct
from common.drawing.table.defaults import TableDefaults

class Table:
    def __init__(self, fields: list = [], title: str = ""):
        if title == "" and len(fields) != 0:
            title = fields.pop(0)
        self.fields = fields
        self.table = TableDefaults(title)
        self.struct = TableStruct()

    def floats(self, symbols: str):
        self.table.float_format = symbols
        return self

    def row(self, x: list):
        self.table.field_names = self.fields
        self.struct.row(self.table, x)
        return self

    def columns(self, start: int, memory):
        self.table.field_names = self.fields
        self.struct.columns(self.table, start, memory)
        return self

    def matrix(self, rows: list, head: str = 'x'):
        self.struct.matrix(self.table, rows, head)
        return self

    def show(self): print(self.table) ; return self

    def clear(self): self.table.clear_rows() ; return self

    def print(self, text: str = ""): print(text) ; return self

    def pause(self, text: str = ""): pause(text) ; return self