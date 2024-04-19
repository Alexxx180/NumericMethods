class Milestone:
    def __init__(self, name: str, args: tuple, size = 100):
        self.base = PointGraphs(-size, size, self.formula)
        self.overlay = PointGraphs(args[0], args[1], self.formula) # Пользовательский интервал
