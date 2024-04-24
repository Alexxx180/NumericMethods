from sympy import Symbol
from sympy.utilities import lambdify

X = Symbol('x')

def formulate(derivative, count: int):
    while count > 0:
        derivative = derivative.diff(derivative)
        count -= 1

    return lambdify(X, derivative)

def derive(text, x, derivative: int):
    formula = formulate(text, derivative)
    return formula(x)
