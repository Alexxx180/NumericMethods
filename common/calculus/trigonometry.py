from sympy import Symbol
from sympy.utilities import lambdify

X = Symbol('x')

def formulate(f, count: int):
    derivative = X
    for i in range(count):
        derivative = f.diff(derivative)
    return lambdify(X, d)

def derive(self, f, x, derivative: int):
    formula = formulate(f, derivative)
    return formula(x)
