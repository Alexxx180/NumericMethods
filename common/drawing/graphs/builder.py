from common.drawing.graphs.canvas import Canvas
from common.drawing.primitives.points import Points
from common.drawing.primitives.point import Point

class CanvasBuilder:
    def __init__(self):
        self.canvas = Canvas()
        self.task = None

    def space(self, space):
        self.canvas.space = space
        return self

    def graph(self, plot, i: int = -1):
        self.canvas.space.set_graph(plot, i)
        return self

    def formula(self, task: callable):
        self.task = task
        return self

    def mark(self, args, size: int = 0):
        if self.task == None:
            self.basis = Point(args, size)
        else:
            self.basis = Points(args, self.task)
        return self

    def label(self, name: str, i: int = -1):
        setting = (name, self.basis, i)
        self.canvas.settings.append(setting)
        return self

    def plane(self, i: int = -1):
        self.canvas.planes.append((self.basis, i))
        return self
