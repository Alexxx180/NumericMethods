import numpy as np

class GaussChecks:
    Text = {
        'none': "\nДанная система не имеет решения.",
        'many': "\nДанная система имеет множество решений.",
        'endless': "Система имеет бесконечное множество решений"
    }

    @static_method
    def __null_string(name: str, row: list):
        return (True, f"Есть нулевая строка " + str(row) + Text[name])

    @static_method
    def __all_zeros(array: list):
        return (all(e == 0 for e in array[:-2]), Text['endless'])

    @staticmethod
    def are_undefined(array):
        shape = array.shape

        for row in array:
            if np.all(row[:-1] == 0) and row[-1] != 0:
                return __null_string(row, 'none')

            if np.all(row == 0):
                return __null_string(row, 'many')

        return __all_zeros(array[shape[0] - 1])

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
