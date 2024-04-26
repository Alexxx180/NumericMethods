class Segment:
    def set_values(self, x: float, sign: float):
        self.x = x
        self.sign = sign

    def __init__(self, x: float, sign: float):
        self.set_values(x, sign)

    def set(self, segment):
        self.set_values(segment.x, segment.sign)

    def update(self, value: float, formula: callable):
        self.x = value
        self.sign = formula(self.x)

    def copy(self):
        return Segment(self.x, self.sign)

    def differs(self, previous) -> bool:
        return self.sign * previous.sign <= 0
