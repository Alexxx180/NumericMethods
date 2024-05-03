from numpy import zeros

class TaskA:
    def __init__(self, args: list):
        self.xy0: tuple = (args[0], args[1])
        self.h: float = args[2]
        self.n: int = args[3]
        self.matrix: list = [zeros(self.n + 1) for i in range(2)]

    def apply(self, f: callable) -> list:
        self.edit(0, self.xy0)
        for j in range(0, self.n):
            k: list = [1, 0, 0, 0, 0]
            for relation in (0.0, 0.5, 0.5, 1.0):
                self.kexpression(f, j, k, relation)

            args: list = [self.h, self.calculate(k)]
            for i in range (0, len(args)):
                args[i] += self.matrix[i][j]

            self.edit(j + 1, args)
        return self.matrix

    def edit(self, j: int, args):
        for i in range(0, len(self.matrix)):
            self.matrix[i][j] = args[i]

    def kexpression(self, f: callable, j: int, k: list, relation: float):
        result: list = [self.h, k[k[0] - 1]]
        for i in range(0, len(result)):
            result[i] = result[i] * relation + self.matrix[i][j]

        k[k[0]] = self.h * f(result[0], result[1])
        k[0] += 1

    def calculate(self, k: list):
        return (k[1] + k[2] * 2 + k[3] * 2 + k[4]) / 6
