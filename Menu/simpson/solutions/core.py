from menu.simpson.solutions.functions import quadratic

class SimpsonCore:
    def __init__(self, ends, f: callable):
        self.factor: int = 2
        self.ends: tuple = ends.start

        self.yends: Ends = ends.based(f)
        self.middle: float = self.yends.sub() / 2 # S в методичке
        self.result: float = self.yends.sum()

    def resize(self, e: float, m: float):
        size: float = self.ends.size()
        self.m: float = m
        self.n: int = quadratic(size, m, e)
        self.size: float = size / self.n # H в методичке

    def coords(self) -> tuple:
        return (self.x, self.y)

    def iteration(self, i: int):
        f: int = self.factor
        self.i: int = i % f
        self.x: float = self.ends.start + i * self.size
        self.y: float = f(x)
        self.result += (f + f * c) * y

    def calculate(self):
        return self.size / 3 * self.result
