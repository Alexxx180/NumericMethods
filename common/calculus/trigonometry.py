from sympy import Symbol
from sympy.utilities import lambdify

X = Symbol('x')

def form(derivative: str) -> str:
    return derivative.diff(X)

def formulate(text, count: int) -> str:
    derivative = text

    try:
        for i in range(count):
            derivative = form(derivative)
    except ValueError:
        return '0'

    return derivative

def invokation(derive: str) -> callable:
    if derive == '0':
        return lambda x: 0
    return lambdify(X, derive)
