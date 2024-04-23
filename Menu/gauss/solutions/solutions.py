import numpy as np
from menu.gauss.solutions.checks import are_undefined
from menu.gauss.solutions.courses.straight import straight
from menu.gauss.solutions.courses.reverse import reverse

class Gauss:
    def __init__(self, num: list):
        self.array = num

    def system_elimination(self):
        n = len(self.array[0])
        a = np.delete(self.array, n - 1, axis=1)
        b = []
        for _, num in enumerate(self.array):
            b.append(float(num[n - 1]))

        n = a.shape[1]

        matrix = straight(n, a, b)
        unresolved = are_undefined(matrix)

        if unresolved[0]:
            print(unresolved[1])

        reverse(n, a, b)
