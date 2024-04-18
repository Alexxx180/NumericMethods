from numpy import linspace
from common.drawing import Points, Graphs, Table
from common.commander.Commander import View
from menu.handlers.func import pause

class TangentInterface:
    def __init__(self, name: str, size: int):
        self.name = name
        self.length = 100
        self.plot = Graphs(1, 1)
        self.base = Points((-size, size), task)
        self.overlay = Points(abe, task)

    def no_roots(a: float, b: float):
        pause(f"Похоже на интервале {[a, b]} корней для функции B нет")

    def memorize(message: str):
        self.message = message
        print(f"\nЗначение m = {message}")

    def output(row: list):
        plot.ax.legend()
        Table(Tangent['Result'], self.message).row(row).show().pause()

    def draw_graph(basis: float, line: float, x: float, y: float, index: int):
        self.plot.ax.plot(basis, line, label=f'Касательная {index}', linestyle='--')
        self.plot.ax.scatter(x, y, color='red', label='её точка')

    def show_graph():
        self.plot.based(self.overlay, f"График {self.name}")
        self.plot.apply(self.base).apply(self.overlay)
        if View('Plot', 'Tangent'):
            self.plot.show()

    def draw_tangent(row: list):
        for index, num in enumerate(row):
            x = float(num[0]); y = float(num[1])

            half = self.length / 2
            points = linspace(x - half, x + half, self.length)
            tangent = float(num[2]) * (points - x) + y

            draw_graph(points, tangent, x, y, index)
        output(row)
