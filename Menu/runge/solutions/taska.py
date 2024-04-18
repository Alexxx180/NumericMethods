import menu.runge.solutions.functions.taska

class Taska:
    @staticmethod
    def formula(x, y):
        return y / (1 + pow(x, 2))

    def __init__(self, arguments: list):
        self.func = TaskaFunctions(arguments)
        self.func.edit(0, arguments)

    def apply(self, f: callable):
        for ii in range(0, self.func.n):
            k = (1, 0, 0, 0, 0)
            r = (0.0, 0.5, 0.5, 1.0)
            for relation in r:
                self.func.kexpression(f, ii, k, relation)

            result = (self.func.calculate(k), h)
            for i in range (0, len(result)):
                result[i] += self.func.get(i, ii)

            self.func.edit(ii + 1, result)

        return self.func.matrix
