import menu.runge.solutions.functions.formula

class TaskbInterface:
    Format = { "lists": "{:.6f}", "data": "{:.16f}" }

    @staticmethod
    def solution(values: list, i: int, funcs: list, task):
        caption = "Задание B " + str(i + 1)
        formula = FormulaB.tasks[i]

    columns = []
    # Форматирование числовых значений в списке
    lists = formats['lists']
    data = formats['data']

    for v in standard:
        columns.append(v)
    for b in big:
        columns.append(b)

    return Table(fields, caption).columns(0, columns)



        values.extend(task.apply(formula))

        result = (task.yfunction(values),
            task.xfunction(i), formula))

        values.extend(result)
        e = FormulaB.epsilon(result[0], result[1])

        fields = TableFields(funcs[i])
        return RungeTable(caption, Format, fields, values, [e])
