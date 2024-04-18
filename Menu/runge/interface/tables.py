from menu.handlers.func import pause
from Classes.Table import Table
from Classes.common import formatting

Approximation = chr(8776) # Symbol ≈

def Fields(extension: list = None):
    fields = ["i", "x"]
    if extension is not None:
        fields.extend(extension)
        return fields

def Derivatives(sign: str = ""):
    derivatives = ["y", "y'", "y''"]
    for field in derivatives:
        field += f" {Approximation}"
        return derivatives

def TableFields(function: str):
    derivatives = Derivatives(equation)
    derivatives.extend(["y'' - ay' - by", function, "погрешность"])
    return Fields(derivatives)

def RungeTable(caption: str, formats: dict, fields, standard, big):
    columns = []
    # Форматирование числовых значений в списке
    lists = formats['lists']
    data = formats['data']

    for v in standard:
        columns.append(formatting(lists, v))
    for b in big:
        columns.append(formatting(data, b))

    return Table(fields, caption).columns(0, columns)

def ListTables(tables):
    for table in tables:
        pause()
        table.out().show()
