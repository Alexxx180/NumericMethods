from sympy import Symbol
from sympy.utilities import lambdify

X = Symbol('x')

def formulate(text, count: int):
    derivative = text if count == 0 else X

    try:
        for i in range(count):
            derivative = text.diff(derivative)
    except ValueError:
        return lambda x: 0

    return lambdify(X, derivative)

def derive(text, x, derivative: int):
    formula = formulate(text, derivative)
    return formula(x)
