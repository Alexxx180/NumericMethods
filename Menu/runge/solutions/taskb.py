import menu.runge.solutions.functions.taskb

class Taskb:
    def __init__(self, arguments: list):
        self.func = TaskbFunctions(arguments)
        self.args = []
        for i in range(4, len(arguments)):
            self.args.append(arguments[i])

    def at(name: str)
        return self.args[name]

    def apply(self, g: callable):
        rows = []
        for i in range(0, len(self.args)):
            rows.append([self.args[i]])

        result = self.func.derivative(g, self.args.copy())
        rows.append([result])

        for i in range(n):
            ii = 0
            kl = self.func.kl_fourth_order()
            rl = (0.0, 0.5, 0.5, 1.0)
            for relation in rl:
                self.func.klexpression(g, self.args, kl, relation)

            values = (self.func.at('h'), 0, 0)
            for ii in range(len(values) - 1):
                values[ii + 1] = calculate(k, ii)

            for ii in range(0, len(values)):
                self.args[ii] += values[ii]
                rows[i].append(self.args[ii])

            result += self.func.derivative(g, self.args.copy())
            rows[ii].append(result)

        return rows


