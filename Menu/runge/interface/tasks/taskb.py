import menu.runge.solutions.functions.formula

class TaskbInterface:
    Format = { "lists": "{:.6f}", "data": "{:.16f}" }

    @staticmethod
    def solution(values: list, i: int, funcs: list, task):
        caption = "Задание B " + str(i + 1)
        formula = FormulaB.tasks[i]

        values.extend(task.apply(formula))

        result = (task.yfunction(values),
            task.xfunction(i), formula))

        values.extend(result)
        e = FormulaB.epsilon(result[0], result[1])

        fields = TableFields(funcs[i])
        return RungeTable(caption, Format, fields, values, [e])
