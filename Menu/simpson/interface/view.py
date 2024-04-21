from common.texts.common import *
from common.calculation.objects import Ends
from common.drawing.graphs import Milestone, DefaultSpace
from menu.simpson.interface import SimpsonInterface

def canvas(ends: tuple, derives: tuple) -> Canvas:
    x = ends.margin(0.5)
    space = ends.margin(10)

    b = CanvasBuilder(name).space(PlainSpace()).graph(Graphs(1, 2))
    b.mark(x, 10).label('Plot 1', 0).label('Plot 2', 1)
    for task in derives:
        b.formula(task).mark(space).plane()

    return b.canvas

def reorder(space, ends, x: float, f: callable):
    y = f(x)
    space.orders.append((x, y))
    space.orders.append((ends, f))

def variables(view: SimpsonInterface):
    pause(Variables['Simpson'].format(view.range.start, view.range.end, view.e, view.solutions.size, view.m, view.n, view.ends.start, view.ends.end, view.result))

def output(view: SimpsonInterface):
    if view.n <= 15 or View('Table', 'Simpson'):
        Table(Simpson['Result']).row(view.solutions.rows).show()
