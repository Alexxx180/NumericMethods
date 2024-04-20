class MilestoneA:
    def __init__(self, name: str, args: tuple, size = 100, formula: callable = None):
        self.name = name
        self.base = PointGraphs(-size, size, formula)
        self.overlay = PointGraphs(args[0], args[1], formula) # Пользовательский интервал

class Milestone:
    def __init__(self, name: str, plot: Point):
        self.name = name
        self.plot = plot
