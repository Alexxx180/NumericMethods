import menu.runge.solutions
import menu.runge.solutions.functions.formula.FormulaA as FA
from menu.runge.interface.tasks.taskb.TaskbInterface import solution
from Classes.Table import Table

class RungeKuttaTasks:
    Precision = 1e-9

    def __init__(self, arguments: list, extension: list = None):
        self.args = arguments

        if extension is not None:
            for i in range(0, len(extension)):
                self.args.insert(i + 2, extension[i])
            self.method = B
        else:
            self.method = A

        numbers = [i for i in range(self.args[3] + 1)]
        self.args.insert(0, numbers)

    def show(name):
        Table(Runge[name]['Source']).row(self.args).show().out()

    def A():
        name = 'A'
        show(name, 'Source')
        task = Taska(self.args)
        values = task.apply(FA.formula)
        values.append(FA.analyze(x))
        values.append(FA.integrate(x).flatten().tolist()) 
        Table(Runge[name]['Result'])

        RungeTable(fields['Result'], values, []).show().pause()

    def B():
        show('B')
        task = Taskb(self.args)
        funcs = ['sin(x)', 'e⁻ˣ', 'cos(x)']
        for i in range(0, len(funcs)):
            solution(self.args, i, funcs, task).pause().out().show()
