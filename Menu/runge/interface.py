import menu.runge.solutions
import menu.runge.solutions.functions.formula.FormulaA as FA
from menu.runge.interface.tasks.taskb.TaskbInterface import solution
from Classes.Table import Table

class RungeKuttaTasks: # Parameters = { 'i': 0, 'x0': 1, 'y0': 2, 'h': 3, 'n': 4 }
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
        self.args.insert(0, numbers) # Parameters['i']

    def A():
        fields = Runge['A']
        Table(fields['Source']).row(self.args).show().out()
        task = Taska(self.args)

        values = task.apply(FA.formula)
        values.append(FA.analyze(x))
        values.append(FA.integrate(x).flatten().tolist()) 
        # Вывод таблицы
        RungeTable(fields['Result'], values, []).show().pause()

    def B(): 
        fields = Runge['B']
        Table(fields['Source']).row(self.args).show().out()
        # a = 2.41, b = 2.18, y' = 1
        task = Taskb(self.args)
        tables = []
        # Решения для функций
        funcs = ['sin(x)', 'e⁻ˣ', 'cos(x)']
        for i in range(0, len(funcs)):
            tables.append(solution(self.args, i, funcs, task))
        # Последовательный вывод всех таблиц
        ListTables(tables)

if __name__ == '__main__':
    print("Не реализована")
