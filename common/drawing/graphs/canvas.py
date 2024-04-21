class Canvas:
    def __init__(self, space, stones: list = []):
        self.orders = []
        self.stones = stones
        self.space = space

    def apply(self):
        for sets in self.canvas.settings:
            self.space.plot.based(sets[0], sets[1], sets[2])

        for plane in self.canvas.planes:
            self.space.plot.apply(plane[0], plane[1])

    def show(self):
        if View('Plot', self.space.name):
            render()
            self.space.show()
            apply()
            self.space.plot.show()
        return self

    def render(self):
        for order in self.orders:
            self.space.render(order)
