class Ends:
    def __init__(self, start: float, end: float):
        self.start = start
        self.end = end

    def size() -> float:
        return self.end - self.start

    def sub() -> float:
        return self.start - self.end

    def sum() -> float:
        return self.start + self.end

    def margin(margin: float = 0.0) -> tuple:
        return (self.start - margin, self.end + margin)
