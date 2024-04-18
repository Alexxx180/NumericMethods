class Segment:
    def set_values(self, x: float, sign: float):
        self.x = x
        self.sign = sign

    def __init__(self, x: float, sign: float):
        set_values(x, sign)

    def set(self, clone: Segment):
        set_values(clone.x, clone.sign)

    def update(self, value: float):
        self.x = value
        self.sign = formula(self.x)

    def differs(self, previous: Segment) -> bool:
        return self.sign * previous.sign <= 0
