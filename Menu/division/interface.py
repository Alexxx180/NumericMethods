from common.commander.formula import *
from common.calculus.trigonometry import formulate, invokation, X
from menu.division.solutions import SegmentDivision
from common.flow.canvas.division import canvas_from
from common.flow.texts.division import Text

def SegmentDivisionMethod(name: str, args: tuple):
    formula = formulate(Formula[name], 0, X)
    derive = invokation(formula, X)

    canvas = canvas_from(name, derive, args)

    division = SegmentDivision(args, derive)

    text = Text(name)
    text.research(formula, division)

    division.study()

    if len(division.roots) == 0:
        text.no_roots()
    else:
        text.source(division.roots).result(division)

    canvas.show(division.orders)
    text.pause()
