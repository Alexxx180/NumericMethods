from menu.runge.interface.solutions import asolution, bsolution
from common.commander.texts.fields import *
from common.drawing.table import Table

class RungeKuttaTasks:
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


    def A():
        asolution(self.args, Taska(self.args))

    def B():
        task = Taskb(self.args)
        funcs = Runge['Functions']
        for i in range(0, len(funcs)):
            bsolution(self.args, i, funcs[i], task)
