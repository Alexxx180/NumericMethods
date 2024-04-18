import numpy as np

from Classes.Table import Table

class GaussFunctions:
    Float = "{:.3f}"

    def format(i: int, k: int, s: str, a):
        no = (f"Строка {i + 1}", f"Строка {k + 1}")
        v = (s.format(a[i][k]), s.format(a[k, k]))
        return "{no[0]} = {no[0]} - {no[1]} * ({v[0]} / {v[1]})"

    # Прямой ход (обнуление элементов ниже главной диагонали)
    def straight_course(n: int, b: list, a, shape):
        table = Table([""], "")
        result = None
        index = 0

        for k in range(n):
            for i in range(k + 1, shape[0]):
                index += 1
                text = format(i, k, Float, a)
                print(f"\nШаг {index}\n{text}")

                ratio = a[i, k] / a[k, k]
                # k: до конца строки
                a[i, k:] -= ratio * a[k, k:]
                b[i] -= ratio * b[k]
                # Добавление столбца
                result = np.column_stack((a, b))
                table.matrix(result).show().clear()

        return result

    # Обратный ход (подстановка обратно, чтобы найти решения)
    def reverse_course(n: int, b: list, a, shape):
        x = np.zeros(n)
        print("\nОбратный ход\n")
        for k in range(shape[0] - 1, -1, -1):
            # np.dot скалярное произведение
            scalar = np.dot(a[k, k + 1:], x[k + 1:])
            x[k] = (b[k] - scalar) / a[k, k]
            print(f"x{k + 1} = {Float.format(x[k])}")
