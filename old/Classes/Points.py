import numpy as np

class Points:
    """Построение графиков"""
    def __init__(self, ends: tuple, func):
        """Свойства точек"""
        self.func = func
        self.a = ends[0]
        self.b = ends[1]
        self.X = []
        self.Y = []
        self.__function()

    def __function(self):
        self.X = [a for a in np.arange(self.a, self.b, 0.0001)]
        self.Y = [self.func(a) for a in self.X]
