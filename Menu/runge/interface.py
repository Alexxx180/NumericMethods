from common.flow.texts.runge import Text
from common.commander.formula import *
from common.calculus.trigonometry import formulate, invokation, integral, X, Y
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

    def __derive(self, formula: str, *symbols) -> callable:
        return invokation(formulate(formula, 0, *symbols), *symbols)

    def __text(self, args):
        return Text(self.name, self.key).source(args)

    def A(self):
        f: callable = self.__derive(self.formula, X, Y)

        columns: list = TaskA(self.args).apply(f)
        columns[0], columns[1] = columns[1], columns[0]

        x: list = columns[0]
        y0: float = self.args[1]

        #integ = integral(self.formula, Y, X)
        #print(integ)
        #i: callable = invokation(integ, Y, X)

        #columns.append([i(y0, x[j]) for j in range(len(x))])
        columns.append(analyze(x))
        columns.append(integrate(x, y0).flatten().tolist())
        #columns.insert(0, [i for i in range(len(x))])

        args = list(self.args)
        args.append(self.formula)
        text = self.__text(args)
        text.result(columns)

    def B(self):
        text = self.__text(self.args)
        task = TaskB(self.args)

        for formula in self.formula:
            f: callable = self.__derive(formula)

            columns: list = task.apply(f)
            x: list = columns[0]
            columns.append(function1(y, task.a, task.b, task.n))
            columns.append(function2(f, x, task.n))
            columns.append(epsilon(result))

            text.result(columns, f, i)
