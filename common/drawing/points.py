from numpy import arrange

class Points:
    def __init__(self, ends: tuple):
        self.func = function
        self.step = 0.0001
        self.a = ends[0]
        self.b = ends[1]
        self.__function()

    def __function(self):
        self.X = [x for x in arange(self.a, self.b, self.step)]
        self.Y = [self.function(x) for x in self.X]

class Point:
    def __init__(self, ends: Ends, margin: float, size: int):
        self.X = ends.margin(margin)
        self.Y = (-size, size)
