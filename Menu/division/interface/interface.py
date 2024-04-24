from common.commander.texts.common import *
from menu.division.solutions.solutions import SegmentDivision
from menu.division.solutions.functions import middle

def Show(name: str, roots: list):
    Table(Division[name]).row(roots).show().pause()

def SegmentDivisionMethod(args: tuple):
    name = 'Division'
    division = SegmentDivision(args)

    print(Texts[name]['Research'].format(
        division.range.start, division.range.end))

    roots = division.study()
    if len(roots) == 0:
        print(Texts[name]['No roots'])
        division.canvas.show()
        return

    Show('Source', roots)
    rows = []

    division.canvas.space.plot.color = "green"

    for index, x in enumerate(roots):
        print(Texts[name]['Interval'].format(one, index + 1, x, division.e))
        division.breakdown(x)

        row = [e for e in x]
        row.append(middle(x))
        rows.append(row)

    Show('Result', rows)
    division.canvas.show()
    pause(Texts[name]['Roots'].format(rows[0][1]))
