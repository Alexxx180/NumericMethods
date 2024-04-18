from menu.handlers.func import pause
from menu.simpson.interface.plots import SimpsonPlots

class SimpsonInterface:
    def __init__(ab: tuple, precision: float):
        self.a = ab[0]
        self.b = ab[1]
        self.e = precision
        self.graph = SimpsonPlots(ab)
        self.root = (0.0, 0.0)

    def out_h(h: float):
        print(f"h = {h}")

    def output(n: int):
        if n <= 15 or View('Table', 'Simpson'):
            Table(Simpson['Result']).row(rows).show()

    def integration(ends: Ends, roots: tuple, result: float):
        pause(f"a = {self.a}, b = {self.b}, e = {self.e:.15f}, M = {roots[0]}," +
            f" n = {roots[1]}\nПределы интегрирования от {ends.start} " +
            f"до {ends.end}\nЗначение интеграла = {result}")
