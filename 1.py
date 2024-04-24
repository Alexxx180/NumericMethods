from sympy import Symbol, sqrt, exp, sin, cos, tan
from sympy.utilities import lambdify

X = Symbol('x')
f = X ** 4 - X - 1

def formulate(text, count: int):
    derivative = text if count == 0 else X

    for i in range(count):
        derivative = text.diff(derivative)

    return lambdify(X, derivative)

def derive(text, x, derivative: int):
    formula = formulate(text, derivative)
    return formula(x)

print(derive(f, 5, 1))
