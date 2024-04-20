from functools import reduce
from operator import sub

class TaskbFunctions:
    def __init__(self, arguments: list):
        params = ('a', 'b', 'n', 'h')
        self.args = init_args(params, arguments)

    def at(name: str)
        return self.args[name]

    def yfunction(self, y):
        result = []
        for i in range(at('n') + 1):
            r = (1, at('a'), at('b'))
            for ii in range(0, 2):
                r[ii] *= y[3 - ii][i]

            result.append(reduce(sub, r))

        return result

    def xfunction(self, f: callable, x: list):
        result = []
        for i in range(at('n') + 1):
            result.append(f(x[i]))
        return result

    # y'' = a * y' + b * y + f(x)
    def derivative(self, fx: callable, row: list): 
        funcs = (lambda yd: yd * at('a'), lambda y: y * at('b'), fx)
        for i in range(0, len(result)):
            row[i] = funcs[i](row[i])
        return sum(result)

    def klexpression(self, f: callable, row: tuple, kl: tuple, relation: float):
        i = kl[0]
        r = (at('h'), kl[i][0], kl[i][1])
        for ii in range(0, len(row)):
            r[ii] = r[ii] * relation + row[ii]

        result = (r[2], f(r[0], r[1], r[2]))
        for ii in range(0, len(result)):
            kl[i][ii] *= result[ii]

        kl[0] = i + 1

    def kl_fourth_order(self):
        h = at('h'); return (1, (h, h) * 4)

    def calculate(self, k: tuple, i: int):
        return (k[1][i] + k[2][i] * 2 + k[3][i] * 2 + k[4][i]) / 6
