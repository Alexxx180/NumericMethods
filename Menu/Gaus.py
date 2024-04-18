import inquirer
import numpy as np

from Gauss_Method.main import gauses

from Classes.Table import Table
from hendllers.func import pause

import Classes.Texts.Queries

# Значения по умолчанию в методе Гауса
def Gaus_defaults():
    defaults = [
        [-1.99, -1.47, -1.05, 3.24, 4.91],
        [-0.79, -1.16, -0.8, -1.15, 7.87],
        [-2.91, -2.72, 3.85, 1.9, 5.78],
        [3.25, 0.98, 0.5, -3.82, 1.0]
    ]
    return defaults

def Gaus():
    A = np.array(Gaus_defaults(), dtype=float) # INPUT

    matrix_A = Table([""], "Исходная матрица")
    matrix_A.matrix(A)
    matrix_A.show()

    defaults = 'Использовать матрицу?'
    question = [inquirer.Confirm('question', message=defaults, default=True)] 
    question = inquirer.prompt(question)

    if question['question']:
        gauses(A)
    else:
        matrix = []
        # Ввод строк матрицы по одной с возможностью завершения ввода
        description = 'Введите строку матрицы (для завершения введите пустую строку)'
        while True:
            row_input = inquirer.prompt([inquirer.Text('row', message=description)])

            # Проверка на завершение ввода
            if not row_input['row']:
                break
            # Обработка введенной строки, разделение на элементы
            try:
                row_values = [float(value) for value in row_input['row'].split()]
            except ValueError:
                ic(ValueError)  # noqa: F821
                print("Неверный ввод")
                pause()
                return 404
            matrix.append(row_values)

            # Проверка на одинаковое количество элементов в строке
            if len(set(map(len, matrix + [row_values]))) > 1:
                print("Ошибка: Вы ввели разное количество элементов")
                pause()
                return 404
            ic(matrix)  # noqa: F821

        matrix = np.array(matrix)
        shape = matrix.shape
        if shape[0] == 1:
            print("Ошибка: Вы ввели одну строку")
            pause()
            return 404
        else:
            # Применение метода
            gauses(matrix) ; ic(matrix)  # noqa: F821
