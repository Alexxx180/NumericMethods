from sympy import Symbol, sqrt, exp, sin, cos, tan

X = Symbol('x')
Y = Symbol('y')

Formula = {
    'Division': X ** 4 - X - 1,
    'Tangent': {
        'A': X ** 3 + 0.2 * X ** 2 + 0.5 * X - 2,
        'B': tan(0.5 * X + 0.1) - X ** 2
    },
    'Simpson': {
        'A': lambda a, b: exp(a * X) * sin(b * X),
        'B': lambda a: 1 / sqrt(X ** 2 + a)
    },
    'Runge': {
        'A': Y / (1 + X ** 2),
        'B': (sin(X), exp(X), cos(X))
    }
}
