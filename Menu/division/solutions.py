from common.calculus.objects.ends import Ends

class SegmentDivision:
    def __init__(self, args: tuple, derive: callable):
        self.roots: list = []
        self.orders: list = []
        self.a: float = args[0]
        self.b: float = args[1]
        self.e: float = args[2]
        self.formula: callable = derive

    def __root(self, i: int, y: float, color: str):
        root: tuple = (i, self.a, self.b)
        self.roots.append(root)

        order: tuple = (self.c, y, color)
        self.orders.append(order)

    def __not_found(self) -> bool:
        return self.b - self.a > self.e

    def study(self):
        self.e *= 2
        self.c: float
        i: int = 0

        while self.__not_found():
            i += 1
            self.c = (self.a + self.b) / 2

            x: float = self.formula(self.a)
            y: float = self.formula(self.c)

            if x * y > 0:
                self.a = self.c
            else:
                self.b = self.c

            color: str = 'blue' if y < 0 else 'red'
            self.__root(i, y, color)

        self.c = (self.a + self.b) / 2
        self.__root(i, y, 'green')
