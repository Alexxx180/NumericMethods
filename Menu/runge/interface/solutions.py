from common.commander.texts.fields import *
from common.commander.formula.formula import *
from menu.runge.solutions.functions.formula import analyze, integrate

def source(name, values):
    Table(Runge[name]['Source']).row(values).show().out()

def asolution(values: list, task):
    name = 'A'
    source(name)

    formula = lambda x: derive(Formula['Runge'][name], x, 0)

    values = task.apply(formula)
    values.append(analyze(x))
    values.append(integrate(x).flatten().tolist())

    Table(Runge[name]['Result']).columns(0, values).show().pause()

def bsolution(values: list, i: int, function: str, task):
    name = 'B'
    source(name)
    
    formula = lambda x: derive(Formula['Runge'][name][i], x, 0)
    
    values.extend(task.apply(formula))

    result = (task.yfunction(values), task.xfunction(i), formula)
    values.extend(result)
    values.append(epsilon(result[0], result[1]))

    fields = Runge[name]['Result']
    fields[0] += str(i + 1)
    fields[7] = function[i]
    Table(fields).columns(0, values).show().pause()
