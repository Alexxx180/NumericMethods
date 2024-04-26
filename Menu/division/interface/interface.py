from common.handlers.printer import Printer
from common.commander.formula.formula import *
from common.commander.texts.fields import *
from common.calculus.trigonometry import formulate, invokation
from menu.division.solutions.solutions import SegmentDivision
from menu.division.solutions.functions import middle
from menu.division.interface.canvas import canvas_from

def SegmentDivisionMethod(name: str, args: tuple):
    formula = formulate(Formula[name], 0)
    derive = invokation(formula)

    division = SegmentDivision(args, derive)
    canvas = canvas_from(name, derive, args)

    text = Printer(name)
    text.add(print, 'Formula', formula)
    text.add(print, 'Research', division.range)

    division.study()
    if len(division.roots) == 0:
        text.add(print, 'No roots').print().clear()
        canvas.show(division.orders)
        return

    grid((name, 'Source'), division.roots)

    rows = []
    for index, values in enumerate(division.roots):
        e: float = division.presision.end
        text.add(print, 'Interval', one, index + 1, values, e)
        division.breakdown(values)

        row = [v for v in values]
        row.append(middle(values))
        rows.append(row)

    grid((name, 'Result'), rows)

    canvas.show(division.orders)
    text.add(pause, 'Roots', rows[0][1]).print().clear()
