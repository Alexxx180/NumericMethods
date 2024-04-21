from numpy import arange

class Points:
    def __init__(self, ends):
        self.func = function
        self.step = 0.0001
        if isinstance(ends, tuple):
            self.a = ends[0]
            self.b = ends[1]
        else:
            self.a = -ends
            self.b = ends
        self.__function()

    def __function(self):
        self.X = [x for x in arange(self.a, self.b, self.step)]
        self.Y = [self.function(x) for x in self.X]

class Point:
    def __init__(self, ends, size: int):
        self.X = ends
        self.Y = (-size, size)

    def margin():
        return (self.X, self.Y)
