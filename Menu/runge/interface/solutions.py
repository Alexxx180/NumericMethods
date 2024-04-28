from common.flow.texts.runge import Text
from common.commander.formula.formula import *
from menu.runge.solutions.functions.formula import analyze, integrate

def asolution(values: list, task):
    name = 'Runge'
    key = 'A'
    text = Text(name)
    text.source(key, values)

    formula = formulate(Formula['Runge', name], 0)
    derive = invokation(formula)

    values = task.apply(derive)
    values.append(analyze(x))
    values.append(integrate(x).flatten().tolist())

    text.result(name, values)

def bsolution(values: list, i: int, task):
    name = 'Runge'
    key = 'B'
    text = Text(name)
    text.source(key, values)

    formula = formulate(Formula['Runge', name, i], 0)
    derive = invokation(formula)

    values.extend(task.apply(derive))

    result = (task.yfunction(values), task.xfunction(i), derive)
    values.extend(result)
    values.append(epsilon(result[0], result[1]))

    text.result(name, values, function, i)
