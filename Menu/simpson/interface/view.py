from common.texts.common import *
from common.calculation.objects import Ends
from common.drawing.graphs import Milestone, DefaultSpace
from menu.simpson.interface import SimpsonInterface

def space(basis: tuple) -> DefaultSpace:
    space = DefaultSpace(Graphs(1,2))
    space.stone = (Milestone(basis, 10), None) * 2
    return space

def reorder(s: DefaultSpace, ends: Ends, x: float, f: callable):
    y = f(x)
    s.orders.append((x, y))
    s.orders.append((ends, f))

def overlay(s: DefaultSpace, canvas: tuple, derives: tuple):
    for i in range(0, len(derives)):
        s.stone[i][1] = Points(canvas, derives[i])

def variables(view: SimpsonInterface):
    pause(Variables['Simpson'].format(view.range.start, view.range.end, view.e, view.solutions.size, view.m, view.n, view.ends.start, view.ends.end, view.result))

def output(view: SimpsonInterface):
    if view.n <= 15 or View('Table', 'Simpson'):
        Table(Simpson['Result']).row(view.solutions.rows).show()

def view(view: SimpsonInterface):
    if View('Plot', 'Simpson'):
        view.space.plot.show()
