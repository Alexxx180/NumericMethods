import numpy as np

from Classes.Table import Table

global_float_format = "{:.3f}"

def check(A):
    shape = A.shape
    ic()  # noqa: F821
    for row in A:
        ic(row) # noqa: F821
        if np.all(row[:-1] == 0) and row[-1] != 0:
            ic()  # noqa: F821
            return f"Есть нулевая строка {row}\nДанная система не имеет решения."
        elif np.all(row == 0):
            ic()  # noqa: F821
            return f"Есть нулевая строка {row}\nДанная система имеет множество решений."
    c = A[shape[0] - 1]
    ic(c) # noqa: F821

    # Проверяем, что все элементы, кроме двух последних, равны нулю
    if all(element == 0 for element in c[:-2]):
        return False
    ic()  # noqa: F821
    return "Система имеет бесконечное множество решений"



def gaussian_elimination(A):
    ic(A)  # noqa: F821
    matrix = Table([""], "Исходная матрица")

    matrix.matrix(A)
    matrix.show()
    n = len(A[0])

    matrix_a = Table([""], "")
    a = np.delete(A, n - 1, axis=1)
    b = []
    for index, num in enumerate(A):
        b.append(num[n - 1])
    ic(A)  # noqa: F821
    ic(a)  # noqa: F821
    ic(b)  # noqa: F821

    shape = a.shape
    n = shape[1]
    ic(shape[0])  # noqa: F821
    index = 1
    # Прямой ход (обнуление элементов ниже главной диагонали)
    ic(n)  # noqa: F821
    for k in range(n):
        ic(k)  # noqa: F821
        for i in range(k + 1, shape[0]):
            ic(k)  # noqa: F821
            print("")
            print(f"Шаг {index}")
            ic(i, k)  # noqa: F821
            print(
                f"Строка {i + 1} = Строка {i + 1} - Строка {k + 1}  * ({global_float_format.format(a[i][k])} / {global_float_format.format(a[k, k])})")
            ic(i)  # noqa: F821
            ratio = a[i, k] / a[k, k]
            ic(ratio)  # noqa: F821
            a[i, k:] -= ratio * a[k, k:]  # k: до конца строки
            b[i] -= ratio * b[k]
            ic(b)  # noqa: F821
            # Добавление столбца
            result_matrix = np.column_stack((a, b))
            ic(result_matrix)  # noqa: F821
            matrix_a.matrix(result_matrix).show().clear()
            index += 1
    ic(a)  # noqa: F821
    c = check(result_matrix)
    if c is not False:
        ic()  # noqa: F821
        return c

    # Обратный ход (подстановка обратно, чтобы найти решения)
    x = np.zeros(n)

    ic(n)  # noqa: F821
    ic(x)  # noqa: F821
    print("\nОбратный ход\n")
    for k in range(shape[0] - 1, -1, -1):
        ic(k)  # noqa: F821
        x[k] = (b[k] - np.dot(a[k, k + 1:], x[k + 1:])) / a[k, k]  # np.dot скалярное произведение
        print(f"x{k + 1} = {global_float_format.format(x[k])}")
    return None
