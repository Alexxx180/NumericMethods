from sympy import Symbol, integrate
from sympy.utilities import lambdify

X = Symbol('x')
Y = Symbol('y')

def form(derivative: str, *symbols) -> str:
    return derivative.diff(*symbols)

def integral(integral: str, *symbols) -> str:
    return integrate(integral, *symbols)

def formulate(text, count: int, *symbols) -> str:
    derivative = text

    try:
        for i in range(count):
            derivative = form(derivative, *symbols)
    except ValueError:
        return '0'

    return derivative

def invokation(derive: str, *symbols) -> callable:
    if derive == '0':
        return lambda x: 0
    return lambdify(symbols, derive)
