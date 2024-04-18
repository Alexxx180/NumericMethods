from Classes.Graphs import Graphs
import menu.division.solutions.division
import menu.division.interface.segment
import menu.division.interface.print

def DivideSegmentMethod(form: dict, tables: tuple, a: float, b: float, n: tuple):
    plot = Graphs(1, 1)

    graph = DivisionSegmentPlot(a, b, plot)
    division = SegmentDivision(plot.ax)

    roots = division.study(a, b, n[0])
    if len(roots) == 0:
        graph.show().print(SegmentPrint.NoRoots)
        return

    tables[0](roots)

    rows = []
    for index, x in enumerate(roots):
        one = form['one']
        intervals(one, index + 1, x, n[1])
        division.breakdown(x, n[1])
        row = (form['list'].format(x), one.format(middle(x)))
        rows.append(row)

    tables[1](rows)
    graph.show().pause(SegmentPrint.Root.format(rows[0][1]))
