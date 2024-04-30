from common.drawing.table.levels import TableLevels

class TableStruct:
    def __init__(self):
        self.levels = TableLevels()

    def row(self, table, values: list):
        levels = self.levels.count(values)
        if levels == 1:
            self.levels.dimension(table, values)
        elif levels > 1:
            self.levels.dimensions(table, values)
        return self

    def rows(self, table, rows: list):
        for row in rows:
            table.add_row(row)

    def column(self, table, i: int, values: list):
        table.add_column(table.field_names[i], values)
        return self

    def columns(self, table, start: int, memory):
        end = len(memory)
        for i in range(start, end):
            column(table, i, memory[i])
        return self

    def matrix(self, table, rows: list, head: str = 'x'):
        fields: list = []
        for i in range(0, len(rows[0]) - 1):
            fields.append(f"{head}{i + 1}")
        fields.append(head.upper())

        table.field_names = fields
        for row in rows:
            table.add_row(row)
