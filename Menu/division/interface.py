from common.commander.formula.formula import *
from common.commander.texts.fields import *
from common.calculus.trigonometry import formulate, invokation
from menu.division.solutions.solutions import SegmentDivision
from menu.division.solutions.functions import middle
from common.flow.canvas.division import canvas_from
from common.flow.texts.division import Text

def SegmentDivisionMethod(name: str, args: tuple):
    formula = formulate(Formula[name], 0)
    derive = invokation(formula)

    canvas = canvas_from(name, derive, args)

    division = SegmentDivision(args, derive)
    division.study()
    roots = division.roots

    text = Text(name)
    text.research(formula, division.range)

    if len(roots) == 0:
        text.no_roots()
        canvas.show(division.orders)
        text.pause()
        return

    text.source(roots)

    for index, values in enumerate(roots):
        e: float = division.presision.end
        text.interval(one, index + 1, values, e)
        division.breakdown(values)

        row = [v for v in values]
        row.append(middle(values))
        text.rows.append(row)

    text.result().roots(rows[0][1])
    canvas.show(division.orders)
    text.pause()
