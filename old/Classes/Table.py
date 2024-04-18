from prettytable import PrettyTable

from menu.handlers.func import pause

class Table:
    def __init__(self, fields: list, title: str = ""):
        """Свойства точек"""
        if title == "":
            title = fields.pop(0)
        self.fields = fields
        self.table = PrettyTable()
        self.table.title = title

    def __single_level(x: list):
        if len(x) != 1:
            self.table.add_row(x)
            return

        for index, num in enumerate(x):
            self.table.add_row([index + 1, num])

    def __dimensions(x: list):
        if len(x[0]) == 2:
            for index, num in enumerate(x):
                self.table.add_row([index + 1, num[0], num[1]]) 
        else:
            for index, num in enumerate(x):
                num.insert(0, index)
                self.table.add_row(num)

    def row(self, x: list):
        """Заполняем таблицу"""
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

    def columns(self, start: int, memory: iterable):
        end = len(memory)
        for i in range(start, end):
            column(i, memory[i])
        return self

    def matrix(self, matrix: list):
        self.table.float_format = ".3"  # .3 означает 3 десятичных знака
        x = []
        for i in range(0, len(matrix[0]) - 1):
            x.append(f"x{i + 1}")
        x.append("X")
        self.table.fields = x
        for row in matrix:
            self.table.add_row(row)

        return self

    def show(self):
        """Выводим таблицу"""
        self.table.float_format = ".8"
        print(self.table)
        return self

    def clear(self):
        self.table.clear_rows()
        return self

    def out(value: str = ""):
        print(value)
        return self

    def pause(self, text: str):
        pause(text)
        return self

    def __count_levels(self, lst):
        if not isinstance(lst, list):
            return 0
        return 1 + max(self.__count_levels(item) for item in lst)
