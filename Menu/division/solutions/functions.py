def middle(x: tuple) -> float:
    return (x[0] + x[1]) / 2

def left(a: float, c: float) -> bool:
    return formula(a) * formula(c) > 0

def change_sequence(x: tuple):
    a: int = 0
    b: int = 1
    c: float = middle(x)
    x[a if left(x[a], c) else b] = c
