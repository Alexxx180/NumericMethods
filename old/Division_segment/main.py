from Classes.Points import PointGraphs
from Classes.Graphs import Graphs
from Classes.Table import Table

from Division_segment.Functions import f, study_function, breakdown
from hendllers.func import pause

global_float_format = "{:.8f}"

# Удобная функция для форматирования с плавающей точкой с использованием глобального формата.
def formatf(value):
    return global_float_format.format(value)

def Division_segment(a, b, n, e):
    plot = Graphs(1, 1) ; ic(a, b, n)  # noqa: F821

    fields1 = ['i', 'Диапазон']
    message = "Интервалы, где найдены корни"
    table_roots = Table(fields1, message)

    fields2 = fields1.copy() 
    fields2.append('Корень')
    message = "Найденные корни"
    table_root = Table(fields2, message)

    base = PointGraphs(-100, 100, f)
    overlay = PointGraphs(a, b, f)

    roots = study_function(a, b, n, plot.ax) ; ic(roots)  # noqa: F821

    if roots is not None:
        # Заполняем таблицу table_roots
        table_roots.add_row(roots) ; ic()  # noqa: F821
        # Выводим table_roots
        table_roots.show()
        pause()

        rows = []
        name = "Определение значения корня "
        for index, num in enumerate(roots):
            ef = formatf(e)
            root = index + 1
            at = num[0]
            to = num[1]

            message = name
            message += f"{root} на интервале {at},"
            message += f"{to} с точностью {ef}\n"
            print(message)

            x_n, x_m = breakdown(at, to, e, plot.ax)
            x_nf = formatf(x_n)
            x_mf = formatf(x_m)
            middle = (x_n + x_m) / 2

            rows.append([f'{x_nf} - {x_mf}', formatf(middle)])
        
        table_root.add_row(rows) ; ic(rows)  # noqa: F821
        table_root.show()

        root = rows[0][1]
        rootf = formatf(float(root))
        print(f"\nF({root}) = {rootf}\n")
        pause()
    else:
        print('Не удалось определить корни на заданном интервале.')
        print('Корней нет / не достаточное разбиение n\nсм. график')

    xp = overlay.X
    yp = overlay.Y

    # Создаем график по пользователькому интервалу
    plot.settings_one("График А", min(xp), max(xp), min(yp), max(yp)) ; ic()  # noqa: F821

    # Создаем график по интервалу -100 100
    plot.Creating_graph_one(base.X, base.Y)
    plot.Creating_graph_one(xp, yp)

    # Показать окно
    plot.show()


if __name__ == '__main__':
    print("Не реализована")
