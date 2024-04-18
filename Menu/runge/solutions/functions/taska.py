from numpy import zeros

class TaskaFunctions:
    def __init__(self, arguments: list):
        self.h = arguments[2]
        self.n = arguments[3]
        self.matrix = zeromatrix()

    def zeromatrix(self):
        return (zeros(self.n), zeros(self.n))

    def get(self, i: int, ii: int):
        return self.matrix[i][ii]

    def edit(self, ii: int, arguments: list):
        for i in range(0, len(self.matrix)):
            self.matrix[i][ii] = arguments[i]

    def kexpression(self, f: callable, ii: int, k: tuple, relation: float):
        i = k[0]

        result = (self.h, k[i - 1])
        for r in range(0, len(result))
            result[r] = result[r] * relation + self.matrix[r][ii]

        k[i] = self.h * f(result[0], result[1])
        k[0] = i + 1

    def calculate(self, k: tuple):
        return (k[1] + k[2] * 2 + k[3] * 2 + k[4]) / 6
