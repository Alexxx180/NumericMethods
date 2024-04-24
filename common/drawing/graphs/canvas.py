from common.commander.switch import View

class Canvas:
    def __init__(self):
        self.orders: list = []
        self.planes: list = []
        self.settings: list = []

    def apply(self):
        for sets in self.settings:
            self.space.plot.based(sets[0], sets[1], sets[2])

        for plane in self.planes:
            self.space.plot.apply(plane[0], plane[1])

    def show(self):
        if View('Plots', self.space.name):
            self.render()
            self.space.show()
            apply()
            self.space.plot.show()
        return self

    def render(self):
        for order in self.orders:
            self.space.render(order)
