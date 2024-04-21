from common.commander.texts.common import *
from menu.division.solutions.solutions import SegmentDivision
from menu.division.solutions.functions import middle

def Show(name: str, roots: list):
    Table(Division[name]).row(roots).show().pause()

def SegmentDivisionMethod(args: tuple):
    division = SegmentDivision(args)
    print(Texts['Research'].format(division.range))

    roots = division.study()
    if len(roots) == 0:
        division.show()
        print(Texts['No roots'])
        return

    Show('Source', roots)
    rows = []

    division.canvas.space.plot.color = "green"

    for index, x in enumerate(roots):
        print(Texts['Interval'].format(one, index + 1, x, division.e))
        division.breakdown(x)

        row = [e for e in x]
        row.append(middle(x))
        rows.append(row)

    Show('Result', rows)
    division.canvas.show()
    pause(Texts['Roots'].format(rows[0][1]))
