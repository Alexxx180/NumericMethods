import numpy as np
import menu.gauss.solutions.checks
from menu.gauss.solutions.functions import straight_course, reverse_course

class Gauss:
    def __init__(self, num: list):
        self.array = num

    # Решение системы уравнений
    def elimination():
        n = len(self.array[0])
        a = np.delete(self.array, n - 1, axis=1)
        b = []
        for _, num in enumerate(self.array):
            b.append(num[n - 1])

        n = a.shape[1]

        matrix = straight_course(n, b, a, a.shape)
        no_solutions = GaussChecks.are_undefined(matrix)

        if no_solutions[0]:
            print(no_solutions[1])

        reverse_course(n, b, a, a.shape)
