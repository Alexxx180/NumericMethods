from Classes.Points import Points
from menu.simpson.solutions.ends import Ends

class SimpsonFunctions:
    @staticmethod
    def search_max(ends: Ends, f: callable, ax):
        points = Points(ends.margin(), f)

        maxed = max(map(abs, points.Y))
        pts = enumerate(points.Y)

        indices = [i for i, value in pts if abs(value) == maxed]
        index = int(indices[0])
        line(points.X[index], f, ax)
        return maxed

    @staticmethod
    def quadratic(size: float, m: float, e: float) -> int:
        n = (m * size ** 5 / (180 * e)) ** 0.25

        if not isinstance(n, int):
            n = int(n + 1)

        while n % 2 != 0:
            n += 1

        return n
