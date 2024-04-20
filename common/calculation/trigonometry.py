from sympy import Symbol, lambidify

class TrigonometryFunctions:
    X = Symbol('x')

    @staticmethod
    def formulate(f, derivative: int):
        d = X
        for i in range(len(derivative)):
            d = f.diff(d)
        return lambdify(X, d)

    @staticmethod
    def derive(self, f, x, derivative: int):
        formula = formulate(f, derivative)
        return formula(x)
