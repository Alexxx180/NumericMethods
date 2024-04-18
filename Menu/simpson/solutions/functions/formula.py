from sympy import Symbol, sqrt, exp, sin

class formula:
    def __init__(self, limits: tuple):
        self.a = limits[0]
        self.b = limits[1]
        self.x = Symbol('x')
        self.tasks = (F1, F2)

    def F1():
        return exp(self.a * self.x) * sin(self.b * self.x)

    def F2(self, x):
        return 1 / sqrt(self.x ** 2 + self.a)
