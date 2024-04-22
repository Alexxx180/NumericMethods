from prettytable import PrettyTable
from common.handlers.interaction import pause

class Table:
    def __init__(self, fields: list = ["", ""], title: str = "", floats: str = ".8"):
        if title == "":
            title = fields.pop(0)
        self.table.float_format = floats
        self.fields = fields
        self.table = PrettyTable()
        self.table.title = title

    def __count_levels(self, lst):
        if not isinstance(lst, list):
            return 0
        return 1 + max(self.__count_levels(item) for item in lst)

    def __append(x: list, add: callable):
        for index, num in enumerate(x):
            add(self.table, index, num)

    def __appendix(t, n, i):
        n.insert(0, i)
        t.add_row(n)

    def __single_level(x: list):
        if len(x) != 1:
            self.table.add_row(x)
        else:
            __append(x, lambda t, i, n: t.add_row([i + 1, n]))

    def __dimensions(x: list):
        if len(x[0]) == 2:
            __append(x, lambda t, i, n: t.add_row([i + 1, n[0], n[1]]))
        else:
            __append(x, __appendix)

    def row(self, x: list):
        self.table.field_names = self.fields

        levels = self.__count_levels(x)
        if levels == 1:
            __single_level(x)
        elif levels > 1:
            __dimensions(x)

        return self

    def column(self, i: int, x: list):
        self.table.add_column(self.field_names[i], x)
        return self

    def columns(self, start: int, memory):
        end = len(memory)
        for i in range(start, end):
            column(i, memory[i])
        return self

    def matrix(self, matrix: list):
        x = []
        for i in range(0, len(matrix[0]) - 1):
            x.append(f"x{i + 1}")
        x.append("X")
        self.table.fields = x
        for row in matrix:
            self.table.add_row(row)

        return self

    def show(self):
        print(self.table)
        return self

    def clear(self):
        self.table.clear_rows()
        return self

    def print(self, text: str = ""):
        print(text)
        return self

    def pause(self, text: str = ""):
        pause(text)
        return self
