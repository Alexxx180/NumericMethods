from inquirer import Confirm, prompt

def are_defaults():
    name = 'confirm'
    message = 'Использовать значения по умолчанию?'
    query = [Confirm(name, message=message, default=True)]
    return prompt(query)[name]

Defaults = { # Значения по умолчанию
    'Division': ( # Метод деления отрезков
        1, 2, 7, 0.01  # a, b, n, e
    ),
    'Tangent': { # Метод Касательных
        'A' : (1.0, 1.2, 0.000001), # a, b, e
        'B' : (0.3, 0.7, 0.000001)  # a, b, e
    },
    'Gauss': ( # Метод Гауса
        (-1.99, -1.47, -1.05, 3.240, 4.91),
        (-0.79, -1.16, -0.80, -1.15, 7.87),
        (-2.91, -2.72, 3.850, 1.900, 5.78),
        (3.250, 0.980, 0.500, -3.82, 1.00)
    ),
    'Runge': { # Формула Рунге-Кутта
        'A': (
            (0, 1, 0.2, 10), # x₀, y₀, h шаг, n кол-во
            (1, 1, 0.2, 10)  # x₀, y₀, h шаг, n кол-во
        ),
        'B': (-4.41, 1.53, 1) # a, b, y'₀
    },
    'Simpson': [ # Формула Симпсона
        (0.73, 1.46, 1, 2, 0.00001), # a, b, start, end, e
        (0.72, 0.00, 1, 2, 0.00001)  # a, b, start, end, e
    ]
}

""" # Switch ON/OFF with '#' at the start of the line

Пример переключателя

""" # Пример матрицы коэффициентов (матрица A) """
