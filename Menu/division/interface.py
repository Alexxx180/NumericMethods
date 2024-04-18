from menu.division.solutions import DivideSegmentMethod
from Classes.Table import Table

form = { 'one': '{:.8f}', 'list', f'{0:.8f} - {1:.8f}' }

def Fields():
    return ['i', 'Диапазон']

def RootIntervals(intervals: list):
    name = 'Интервалы с корнями'
    Table(Fields(), name).row(intervals).show().pause()

def FoundedRoots(roots: list):
    fields = Fields()
    fields.append('Корень')
    Table(fields, 'Найденные корни').row(roots).show().pause()

def DivideSegment(a, b, n, e):
    tables = (RootIntervals, FoundedRoots)
    DivideSegmentMethod(form, tables, a, b, (n, e))

if __name__ == '__main__':
    print("Не реализована")
