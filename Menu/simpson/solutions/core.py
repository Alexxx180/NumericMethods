class SimpsonCore:
    def __init__(ends: Ends, n: int, f: callable):
        self.factor: int = 2

        self.size: float = ends.size() / n # H в методичке
        self.start: float = ends.start
        self.end: float = ends.end

        self.yends = Ends(f(ends.start), f(ends.end))
        self.middle: float = self.yends.sub() / 2 # S в методичке
        self.result: float = self.yends.sum()

    def iteration(i: int):
        f: int = self.factor
        self.i: int = i % f
        self.x: float = self.start + i * self.size
        self.y: float = f(x)
        self.result: float += (f + f * c) * y

    def calculate():
        return self.size / 3 * self.result
