from common.calculus.objects.ends import Ends
from common.drawing.graphs.spaces.plain import PlainSpace
from common.drawing.graphs.builder import CanvasBuilder
from common.drawing.graphs.graphs import Graphs

def canvas_from(name: str, ends, derives: list):
    base: tuple = ends.margin(10)
    x: tuple = ends.margin(0.5)
    count: int = len(derives)

    graph = Graphs(1, 2)
    space = PlainSpace(name)

    builder = CanvasBuilder()
    builder.space(space)
    builder.graph(graph)
    builder.mark(x, 10)

    for i in range(count):
        builder.label(f'Plot {i + 1}', i)

    for i in range(count):
        builder.formula(derives[i]).mark(base).plane(i)

    builder.entitle('Full Name')
    return builder.canvas
