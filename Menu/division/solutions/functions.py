def middle(x: tuple) -> float:
    return (x[0] + x[1]) / 2

def left(a: float, c: float) -> bool:
    return formula(a) * formula(c) > 0

def swap(x: tuple):
    a: int = 0
    b: int = 1
    c: float = middle(x)
    x[a if left(x[a], c) else b] = c

def resign(root: list, segments: tuple, interval: list) -> str:
    if segments[1].differs(segments[0]):
        roots.append(interval)
        return 'blue'
    return 'red'

def sequence(change: callable, x: tuple, f: callable) -> tuple:
    color: str = 'green'
    order: tuple = (x, f(x), color)
    change(x)
    print(x)
    return order
