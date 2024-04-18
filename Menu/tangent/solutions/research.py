class Research:
    def __init__(self, task)
        self.a = (0, 0, 0, 0)
        self.b = (0, 0, 0, 0)
        self.task = task
        self.message = ""
        self.roots = None

    def side(name: str, direction: tuple):
        d2 = direction[2] ; d3 = direction[3]

        if d2 != 0 or d3 != 0:
            self.roots = (direction[0], self.m)
            self.message = f"{self.m}"
        else:
            self.message = f"f'({name}) = {d2}, f''({name}) = {d3}"

    def problem():
        a = self.a[1] ; b = self.b[1]
        self.message = f"f(a) * f(b) = {a} * {b} = {a * b} > 0"

    def descent():
        self.m = min(abs(self.a[2]), abs(self.b[2]))

        if self.a[1] * self.a[3] > 0:
            side('a', self.a)
        elif self.b[1] * self.b[2] > 0:
            side('b', self.b)

        return problem()

    def start(ab: tuple):
        self.a[0] = ab[0]
        self.b[0] = ab[1]

        for i in range(1, len(self.a)):
            self.a[i] = derive(self.task, self.a[0], i)
            self.b[i] = derive(self.task, self.b[0], i)

        if ab[0] * ab[1] < 0:
            descent()
        else:
            self.message = problem()
