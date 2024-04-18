import menu.division.solutions.functions
import menu.handlers.func
from Classes.Points import PointGraphs

class SegmentDivisionPlot:
    def __init__(self, a: float, b: float, plot):
        self.name = 'График A'
        self.a = a
        self.b = b
        self.plot = plot
        self.base = PointGraphs(-100, 100, DivisionFunctions.formula)
        # Пользовательский интервал
        self.overlay = PointGraphs(a, b, DivisionFunctions.formula) 

    def start():
        print("\nЗапуск исследования функции",
            f'исследуем интервал от {self.a} до {self.b}')

    def show():
        self.plot.based(self.name, overlay)
        self.plot.apply(base).apply(overlay).show()
        return self

    def pause(text: str):
        pause(text)

    def print(text: str):
        print(text)

    @staticmethod
    def intervals(f: str, no: int, limits: tuple, precision: int)
        print('Определение значения корня {no}' +
            f' на интервале {limits[0]}, {limits[1]}' +
            f' с точностью {f.format(precision)}\n')
