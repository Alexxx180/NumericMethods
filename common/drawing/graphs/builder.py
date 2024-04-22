class CanvasBuilder:
    def __init__(self, name: str):
        self.name = name
        self.labels = Texts[name]
        self.canvas = Canvas()
        self.task = None

    def space(space):
        self.space = space
        self.space.name = self.name
        return self

    def graph(plot, i: int = -1):
        self.space.set_graph(plot, i)

    def formula(task: callable):
        self.task = task
        return self

    def mark(args, size: int = 0):
        if self.task == None:
            self.basis = Point(args, size)
        else:
            self.basis = Points(args, self.task)
        return self

    def label(name: str, i: int = -1):
        stone = (name, self.basis, i)
        self.canvas.settings.append(sets)
        return self

    def plane(i: int = -1):
        self.canvas.planes.append((self.basis, i))
        return self

    def apply(self, i: int = -1):
        for sets in self.canvas.settings:
            plot.based(sets[0], sets[1], sets[2])

        for plane in self.canvas.planes:
            plot.apply(plane[0], plane[1])
