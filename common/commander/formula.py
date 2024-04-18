from sympy import Symbol, sqrt, exp, sin, tan

X = Symbol('x')

Formula = {
    'Tangent': {
        'A': lambda: X ** 3 + 0.2 * X ** 2 + 0.5 * X - 2,
        'B': lambda: tan(0.5 * X + 0.1) - X ** 2
    },
    'Simpson': {
        'A': lambda a, b: exp(a * X) * sin(b * X),
        'B': lambda a: 1 / sqrt(X ** 2 + a)
    }
}
