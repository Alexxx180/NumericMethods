from sympy.abc import x, y
from common.flow.texts.runge import Text
from common.commander.resources import Resources
from common.calculus.trigonometry import formulate, invokation, express
from menu.runge.solutions.functions import analyze, function1, function2, epsilon
from menu.runge.solutions.taska import TaskA
from menu.runge.solutions.taskb import TaskB

class RungeKuttaTasks:
    def __init__(self, name: str, key: str, args: tuple):
        self.name = name
        self.key = key
        self.args = args
        self.formula = Resources.Formula[self.name][self.key]
        self.method = getattr(self, key)

    def __derive(self, formula: str, *symbols) -> callable:
        return invokation(express(formula), *symbols)

    def __text(self, args):
        return Text(self.name, self.key).source(args)

    def A(self):
        f: callable = self.__derive(self.formula, x, y)
        columns: list = TaskA(self.args).apply(f)

        X: list = columns[0]
        y0: float = self.args[1]
        h: float = self.args[2]

        columns.append(analyze(h, X, y0, f))

        args = list(self.args)
        args.append(self.formula)
        text = self.__text(args)
        text.result(columns)

    def B(self):
        text = self.__text(self.args)
        task = TaskB(self.args)

        for formula in self.formula:
            f: callable = self.__derive(formula, x)
            length: int = task.n + 1
            columns: list = task.apply(f)
            X: list = columns[0]

            columns.append(function1(columns, task.a, task.b, length))
            columns.append(function2(f, X, length))
            columns.append(epsilon(columns, length))

            text.result(columns, str(formula))
