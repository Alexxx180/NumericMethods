from common.commander.texts.common import *
from common.calculus.objects.ends import Ends
from common.drawing.graphs.spaces.plain import PlainSpace

def canvas(ends: tuple, derives: tuple):
    x: tuple = ends.margin(0.5)
    space: tuple = ends.margin(10)
    count: int = len(derives)

    b = CanvasBuilder().space(PlainSpace(name))
    b.graph(Graphs(1, 2)).mark(x, 10)
    for i in range(count):
        b.label(f'Plot {i + 1}', i)

    for i in range(count):
        b.formula(derives[i]).mark(space).plane(i)

    return b.canvas

def reorder(space, ends, x: float, f: callable):
    y = f(x)
    space.orders.append((x, y))
    space.orders.append((ends, f))

def variables(view):
    pause(Variables['Simpson'].format(view.range.start, view.range.end, view.e, view.solutions.size, view.m, view.n, view.ends.start, view.ends.end, view.result))

def output(view):
    if view.n <= 15 or View('Table', 'Simpson'):
        Table(Simpson['Result']).row(view.solutions.rows).show()
