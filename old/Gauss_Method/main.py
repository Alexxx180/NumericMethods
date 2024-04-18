from Gauss_Method.Functions import gaussian_elimination
from hendllers.func import pause

def gauses(A):
    # Пример матрицы коэффициентов (матрица A) и вектора свободных членов (вектор b)
    #A = np.array([[-0.40, 2.16, -2.90, 0.49, 2.18],
    #              [-2.42, -2.86, 0.75, 3.73, 4.41],
    #              [2.54, -3.01, -3.36, -1.24, 9.04],
    #              [-2.78, -3.35, -0.11, -1.88, 0.70]],
    #            dtype=float)

    #A = np.array([[1,2,3, 6],
    #            [2,-1,-1,3],
    #            [-3,2,-2,-5]],
    #            dtype=float)

    shape = A.shape
    if shape[0] <= shape[1] -1:
        # Решение системы уравнений
        x =gaussian_elimination(A)
        if x is not None:
            print("")
            print(x)
    else:
        print("Нет решения")
    pause()


if __name__ == '__main__':
    print("Не реализована")
