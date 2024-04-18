from sympy import Symbol, tan

class TangentFormula:
    def __init__(self, name: str):
        tasks = { 'A': A, 'B': B }

        self.x = Symbol('x')
        self.tasks = tasks[name]

    def A(self):
        return self.x ** 3 + 0.2 * self.x ** 2 + 0.5 * self.x - 2

    def B(self):
        return tan(0.5 * self.x + 0.1) - self.x ** 2
