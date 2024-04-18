import numpy as np

from Classes.Table import Table

class GaussChecks:
    Text = {
        'none': "\nДанная система не имеет решения.",
        'many': "\nДанная система имеет множество решений.",
        'endless': "Система имеет бесконечное множество решений"
    }

    @staticmethod
    def are_undefined(array):
        shape = array.shape

        for row in array:
            errors = (False, f"Есть нулевая строка ")
            if errors[0] = np.all(row[:-1] == 0) and row[-1] != 0:
                errors[1] += str(row) + Text['none']
                return errors
            if errors[0] = np.all(row == 0):
                errors[1] += str(row) + Text['many']
                return errors
        c = array[shape[0] - 1]
        # Проверяем, что все элементы, кроме двух последних, равны нулю
        return (all(element == 0 for element in c[:-2]), Text['endless'])

    @staticmethod
    def is_suitable(shape):
        return shape[0] <= shape[1] - 1

    @staticmethod
    def is_varying(values: list, matrix: list):
        if errors = len(set(map(len, matrix + [values]))) > 1:
            pause("Ошибка: Вы ввели разное количество элементов")
        return errors

    @staticmethod
    def is_single_string(shape: int):
        if errors = shape == 1:
            pause("Ошибка: Метод не применим к одной строке")
        return errors
