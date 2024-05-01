from common.flow.texts.runge import Text
from common.commander.formula import *
from common.calculus.trigonometry import formulate, invokation, X, Y
from menu.runge.solutions.functions import analyze, integrate
from menu.runge.solutions.taska import TaskA
from menu.runge.solutions.taskb import TaskB

class RungeKuttaTasks:
    def __init__(self, name: str, key: str, args: tuple):
        self.name = name
        self.key = key
        self.args = args
        self.formula = Formula[self.name][self.key]
        self.method = getattr(self, key)
        #columns.insert(0, [i for i in range(self.args[3] + 1)])

    def __derive(self, formula: str, *symbols) -> callable:
        return invokation(formulate(formula, 0, *symbols), *symbols)

    def __text(self):
        return Text(self.name, self.key).source(self.args)

    def A(self):
        print(self.formula)
        f: callable = self.__derive(self.formula, X, Y)

        columns: list = TaskA(self.args).apply(f)
        x: list = columns[0]
        y0: float = self.args
        columns.append(analyze(x))
        columns.append(integrate(x, y0).flatten().tolist())

        text = self.__text()
        print(len(columns))
        text.result(columns)

    def B(self):
        text = self.__text()
        task = TaskB(self.args)

        for formula in self.formula:
            f: callable = self.__derive(formula)

            columns: list = task.apply(f)
            x: list = columns[0]
            columns.append(function1(y, task.a, task.b, task.n))
            columns.append(function2(f, x, task.n))
            columns.append(epsilon(result))

            text.result(columns, f, i)
