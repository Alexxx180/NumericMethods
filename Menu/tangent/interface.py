from Classes.Points import Points
from Classes.Graphs import Graphs
from Classes.Table import Table
from common.commander import Commander
from menu.handlers.func import pause

class TangentInterface:
    def __init__(self, name: str, size: int):
        self.name = name
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
        if Commander.View('Plot', 'Tangent'):
            self.plot.show()
