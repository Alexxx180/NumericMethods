from Classes.Points import PointGraphs
from Classes.Graphs import Graphs
from Classes.Table import Table

from Tangent_method.Functions import f_a, f_a_s, f_a_s_s, f_b, f_b_s, f_b_s_s, tangent_g, research, tangent
from hendllers.func import pause


def Tangent_method_common(a, b, e, task, f_main, f1, f2):
    plot = Graphs(1, 1) ; ic(a, b, e)  # noqa: F821

    fields = ["ᵢ", "x", "F(xᵢ)", "F'(xᵢ)", "|F(xᵢ)| / m"]
    message = f"Результаты вычислений {task} представлены в следующей таблице:"

    table = Table(fields, message) ; ic()  # noqa: F821


    # Исследуем функцию B
    x, m = research(a, b, f_main, f1, f2) ; ic(x)  # noqa: F821

    print("\nЗначение m = ", m)

    if x is not None and m is not None:
        row = tangent(e, m, x, f_main, f1)
        tangent_g(row, plot.ax)
        table.add_row(row)
        # Выводим table_roots
        table.show()
        # Добавление легенды
        plot.ax.legend()
    else:
        print(f"Похоже на интервале {[a, b]} корней для функции B нет")
    pause()

    xp = overlay.X
    yp = overlay.Y

    base = PointGraphs(-100, 100, f_main)
    overlay = PointGraphs(a, b, f_main) ; ic()  # noqa: F821

    plot.settings_one(f"График {task}", min(xp), max(xp), min(yp), max(yp))

    # Создаем график по интервалу -100 100
    plot.Creating_graph_one(base.X, base.Y)
    plot.Creating_graph_one(overlay.X, overlay.Y)

    # Показать окно
    # plot.show()

def Tangent_method_b(a, b, e):
    Tangent_method_common(a, b, e, "B", f_b, f_b_s, f_b_s_s)

def Tangent_method_a(a, b, e):
    Tangent_method_common(a, b, e, "A", f_a, f_a_s, f_a_s_s)

if __name__ == '__main__':
    print("Не реализована")
