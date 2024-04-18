from Runge_Kutta.Functions import metod, func_a, format_list, analytical_solution, diff_eq, g1, g2, g3, B, epsilon
from hendllers.func import pause
from Classes.Table import Table

from scipy.integrate import odeint

list_format = "{:.6f}"
big_list_format = "{:.16f}"

def Runge_Kutta_A(x_0, y_0, h, n):
    # Начальные условия
    # x_0 = 0  # Начальное значение x
    # y_0 = 0  # Начальное значение y (y(x0) = y0)
    # h = 0.2  # Шаг интегрирования
    # n = 10  # Количество шагов

    table_0 = Table(["x₀", "y₀", "h", "n"], "Условия")
    table_0.add_row([x_0, y_0, h, n])
    table_0.show()
    print("")

    x, y = metod(func_a, x_0, y_0, h, n)

    # Аналитическое решение
    y_analytical = analytical_solution(x)

    # Интегрирование уравнения с odeint и функцией f
    y_solution = odeint(diff_eq, y_0, x, rtol=1e-9, atol=1e-9)
    y_solution_list = y_solution.flatten().tolist()

    # ФОРМАТИРОВАНИЯ ЦИСЛОВЫХ ЗНАЧЕНИЙ В СПИСКЕ
    x = format_list(list_format, x)
    y = format_list(list_format, y)
    y_analytical = format_list(list_format, y_analytical)
    y_solution_list = format_list(list_format, y_solution_list)

    i = [a for a in range(n + 1)]

    ic(x, y)  # noqa: F821
    ic(y_analytical)  # noqa: F821
    ic(y_solution_list)  # noqa: F821

    # Вывод табцицы
    table = Table(["i", "x", f"y {chr(8776)}", "y_an =", "y_pr = "], "Задание А")
    table.add_column(0, i)
    table.add_column(1, x)
    table.add_column(2, y)
    table.add_column(3, y_analytical)
    table.add_column(4, y_solution_list)

    table.show()

    pause()


def Runge_Kutta_B(x_0, y_0, yp_0, h, n, a, b):
    # a = 2.41
    # b = 2.18
    # yp_0 = 1

    table_0 = Table(["x₀", "y₀", "y'₀", "a", "b", "h", "n"], "Условия")
    table_0.add_row([x_0, y_0, yp_0, a, b, h, n])
    table_0.show()
    print("")

    # ЗАДАНИЕ B

    b = B(a, b, n, h, x_0, y_0, yp_0)

    i = [a for a in range(n + 1)]

    # Решение для первой функции g(x) = sin(x)
    x_values_1, y_values_1, yp_values_1, ypp_values_1 = b.runge_kutta(g1)

    res1_1 = b.f_1(ypp_values_1, yp_values_1, y_values_1)
    res2_1 = b.f_2(x_values_1, g1)
    e_1 = epsilon(res1_1, res2_1)

    x_values_1 = format_list(list_format, x_values_1)
    y_values_1 = format_list(list_format, y_values_1)
    yp_values_1 = format_list(list_format, yp_values_1)
    ypp_values_1 = format_list(list_format, ypp_values_1)
    res1_1 = format_list(list_format, res1_1)
    res2_1 = format_list(list_format, res2_1)
    e_1 = format_list(big_list_format, e_1)
    
    fields = ["i", "x", f"y {chr(8776)}", f"y' {chr(8776)}", f"y'' {chr(8776)}",
        "y'' - ay' - by", "", "погрешность"]
    no = 6

    fields1 = fields.copy()
    fields1[no] = 'sin(x)'
    # ТАБЛИЦА 1
    table_b_1 = Table(fields1, "Задание B 1")
    table_b_1.add_column(0, i)
    table_b_1.add_column(1, x_values_1)
    table_b_1.add_column(2, y_values_1)
    table_b_1.add_column(3, yp_values_1)
    table_b_1.add_column(4, ypp_values_1)
    table_b_1.add_column(5, res1_1)
    table_b_1.add_column(6, res2_1)
    table_b_1.add_column(7, e_1)

    ic()  # noqa: F821

    # Решение для второй функции g(x) = e^(-x)
    x_values_2, y_values_2, yp_values_2, ypp_values_2 = b.runge_kutta(g2)

    res1_2 = b.f_1(ypp_values_2, yp_values_2, y_values_2)
    res2_2 = b.f_2(x_values_2, g2)
    e_2 = epsilon(res1_2, res2_2)

    x_values_2 = format_list(list_format, x_values_2)
    y_values_2 = format_list(list_format, y_values_2)
    yp_values_2 = format_list(list_format, yp_values_2)
    ypp_values_2 = format_list(list_format, ypp_values_2)
    res1_2 = format_list(list_format, res1_2)
    res2_2 = format_list(list_format, res2_2)
    e_2 = format_list(big_list_format, e_2)

    # ТАБЛИЦА 2
    fields2 = fields.copy()
    fields2[no] = 'e⁻ˣ'
    table_b_2 = Table(fields2, "Задание B 2")
    table_b_2.add_column(0, i)
    table_b_2.add_column(1, x_values_2)
    table_b_2.add_column(2, y_values_2)
    table_b_2.add_column(3, yp_values_2)
    table_b_2.add_column(4, ypp_values_2)
    table_b_2.add_column(5, res1_2)
    table_b_2.add_column(6, res2_2)
    table_b_2.add_column(7, e_2)

    ic()  # noqa: F821

    # Решение для третьей функции g(x) = cos(x)
    x_values_3, y_values_3, yp_values_3, ypp_values_3 = b.runge_kutta(g3)

    res1_3 = b.f_1(ypp_values_3, yp_values_3, y_values_3)
    res2_3 = b.f_2(x_values_3, g3)
    e_3 = epsilon(res1_3, res2_3)

    x_values_3 = format_list(list_format, x_values_3)
    y_values_3 = format_list(list_format, y_values_3)
    yp_values_3 = format_list(list_format, yp_values_3)
    ypp_values_3 = format_list(list_format, ypp_values_3)
    res1_3 = format_list(list_format, res1_3)
    res2_3 = format_list(list_format, res2_3)
    e_3 = format_list(big_list_format, e_3)

    # ТАБЛИЦА 3
    fields3 = fields.copy()
    fields3[no] = 'cos(x)'
    table_b_3 = Table(fields3, "Задание B 3")
    table_b_3.add_column(0, i)
    table_b_3.add_column(1, x_values_3)
    table_b_3.add_column(2, y_values_3)
    table_b_3.add_column(3, yp_values_3)
    table_b_3.add_column(4, ypp_values_3)
    table_b_3.add_column(5, res1_3)
    table_b_3.add_column(6, res2_3)
    table_b_3.add_column(7, e_3)

    table_b_1.show()
    pause()
    print("")
    table_b_2.show()
    pause()
    print("")
    table_b_3.show()
    pause()


if __name__ == '__main__':
    print("Не реализована")
