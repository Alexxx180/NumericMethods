from Runge_Kutta.Runge_Kutta import Runge_Kutta_A, Runge_Kutta_B
from Classes.Input import vinput
import Classes.Texts.Queries as q

class RungeKutta:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

    # Значения по умолчанию в формуле Рунге-Кутта
    # Начало x₀, y₀, h шаг, n кол-во
    def runge_kutta_defaults(form):
        defaults = [
            [ 0,  1,   0.2,  10],
            [ 1,  1,   0.2,  10]
        ]
        c = defaults[form - 1]
        return c[0], c[1], c[2], c[3]

    # Начало      a,     b,  y'₀
    def runge_kutta_defaults_b():
        return -4.41, 1.53,  1

    def runge_kutta_input():
        request = vinput(q.x_y_h_n_request)
        x0 = float(request['variable_x'])
        y0 = float(request['variable_y'])
        h = float(request['variable_h'])
        n = int(request['variable_n'])
        return x0, y0, h, n

    def runge_kutta_input_b():
        request = vinput(q.yp_a_b_request)
        yp_0 = float(request['variable_yp'])
        a = float(request['variable_a'])
        b = float(request['variable_b'])
        return x0, y0, h, n

    def runge_kutta(form):
        form1 = form == 1
        if (not form1) and form != 2:
            return

        defaults = vinput(q.confirm)['confirm']

        if defaults:
            x_0, y_0, h, n = runge_kutta_defaults(form)
        else:
            x_0, y_0, h, n = runge_kutta_input()

        if form1:
            # Применение метода A
            Runge_Kutta_A(x_0, y_0, h, n)
        else:
            if defaults:
                a, b, yp_0 = runge_kutta_defaults_b()
            else:
                a, b, yp_0 = runge_kutta_input_b()

            # Применение метода B
            Runge_Kutta_B(x_0, y_0, yp_0, h, n, a, b)
