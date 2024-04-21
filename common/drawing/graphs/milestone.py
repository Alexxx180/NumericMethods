from common.drawing.points import Points

class MilestoneA:
    def __init__(self, name: str, args: tuple, size = 100, formula: callable = None):
        self.name = name
        self.base = Points(-size, size, formula)
        self.overlay = Points(args[0], args[1], formula) # Пользовательский интервал

class Milestone:
    def __init__(self, name: str, plot):
        self.name = name
        self.plot = plot
