from menu.runge.solutions.functions import kl_order, derivative, calculate

class TaskB:
    def __init__(self, args: list):
        self.a: float = args[0]
        self.b: float = args[1]
        self.y0: list = [args[i] for i in range(2, 5)]
        self.h: float = args[5]
        self.n: float = args[6]

    def __append(self, rows: list, kl: list, i: int, value: float):
        self.y[i] += value
        rows[i].append(self.y[i])

    def apply(self, f: callable):
        self.y: list = self.y0.copy()
        result: float = derivative(self.y, self.a, self.b, f)

        rows: list = [[y] for y in self.y]
        rows.append([result])

        for i in range(self.n):
            kl: list = kl_order(self.h)
            for relation in (0.0, 0.5, 0.5, 1.0):
                self.klexpression(f, kl, relation)

            self.__append(rows, kl, 0, self.h)
            for j in range(1, 3):
                self.__append(rows, kl, j, calculate(kl, j - 1))

            result += derivative(self.y, self.a, self.b, f)
            rows[3].append(result)

        return rows

    def klexpression(self, f: callable, kl: list, relation: float):
        i: int = kl[0]
        r: list = (kl[i] if i == 1 else kl[i - 1]).copy()
        r.insert(0, self.h)
        for j in range(0, len(self.y)):
            r[j] = r[j] * relation + self.y[j]

        kl[i][0] *= r[2]
        kl[i][1] *= derivative(r, self.a, self.b, f)
        kl[0] += 1
