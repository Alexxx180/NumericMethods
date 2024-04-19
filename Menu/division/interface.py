import menu.division.solutions.division
import menu.division.interface.segment
from menu.division.interface.print import start, intervals, no_roots
from menu.division.solutions.functions import middle

def Show(name: str, roots: list):
    Table(Division[name]).row(name).show().pause()

def DivideSegmentMethod(args: tuple):
    division = SegmentDivision(args)
    start(division.range)

    roots = division.study()
    if len(roots) == 0:
        division.show()
        no_roots()
        return

    Show('Source', roots)
    rows = []

    division.space.plot.color = "green"

    for index, x in enumerate(roots):
        intervals(one, index + 1, x, division.e)
        division.breakdown(x)

        row = [e for e in x]
        row.append(middle(x))
        rows.append(row)

    Show('Result', rows)
    division.show()
    pause(Root.format(rows[0][1]))
