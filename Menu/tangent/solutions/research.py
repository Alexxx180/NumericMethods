from common.commander.texts.common import *
from common.commander.formula.formula import *
from common.calculus.trigonometry import formulate

class Research:
    def __init__(self, key: str, name: str):
        self.a: list = []
        self.b: list = []
        self.derives: list = []
        self.name = name
        for i in range(0, 3):
            formula = formulate(Formula[name][key], i)
            derive = lambda x: formula(x)
            self.derives.append(derive)
        self.message = ""
        self.roots = None

    def side(self, name: str, direction: tuple):
        d2 = direction[2] ; d3 = direction[3]

        if d2 != 0 or d3 != 0:
            self.roots = (direction[0], self.m)
            self.message = str(self.m)
        else:
            self.message = Texts[self.name]['Derivatives'].format(name, d2, d3)

    def problem(self):
        self.message = Texts[self.name]['Problem'].format(self.a[1], self.b[1])

    def descent(self):
        self.m = min(abs(self.a[2]), abs(self.b[2]))

        if self.a[1] * self.a[3] > 0:
            self.side('a', self.a)
        elif self.b[1] * self.b[2] > 0:
            self.side('b', self.b)

        return self.problem()

    def start(self, ab: tuple):
        for derive in self.derives:
            self.a.append(derive(ab[0]))
            self.b.append(derive(ab[1]))

        if ab[0] * ab[1] < 0:
            descent()
        else:
            self.message = self.problem()
