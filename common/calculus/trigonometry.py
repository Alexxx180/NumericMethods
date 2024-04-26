from sympy import Symbol
from sympy.utilities import lambdify

X = Symbol('x')

def formulate(text, count: int):
    derivative = text if count == 0 else X

    try:
        for i in range(count):
            derivative = text.diff(derivative)
    except ValueError:
        return '0'

    return derivative

def invokation(derive):
    if derive == '0':
        return lambda x: 0
    return lambdify(X, derive)
