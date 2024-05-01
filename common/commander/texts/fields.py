from common.drawing.table.table import Table

#a = chr(8776) # Approximation Symbol ≈

Fields = {
    'Runge': {
        'A': {
            'Source': ['Условия', 'x₀', 'y₀', 'h', 'n', 'Формула'],
            'Result': ['Задание А', 'xᵢ', f'y ≈', 'yₐₙ =', 'yₚᵣ = ']
            #'ᵢ', 'x', f'y ≈', 'yₐₙ =', 'yₚᵣ = ']
        },
        'B': {
            'Source': ['Условия', 'x₀', 'y₀', 'y’₀', 'a', 'b', 'h', 'n'],
            'Result': ['Задание B', 'i', 'x', f'y ≈', f'y’ ≈', f'y’’ ≈', 'y’’ - ay’ - by', 'f(x)', 'погрешность'],
            'Functions': ['sin(x)', 'e⁻ˣ', 'cos(x)']
        }
    },
    'Gauss' : {
        'Source': ["Исходная матрица", ""]
    },
    'Tangent' : {
        'Formula': ['Производные', 'Функция', 'Уравнение'],
        'Result': ['Результаты вычислений', 'xᵢ', 'F(xᵢ)', 'F’(xᵢ)', '|F(xᵢ)| / m'], 
    },
    'Simpson' : {
        'Result': ['Результаты', 'xᵢ', 'xᵢ четное', 'xᵢ нечетное']
        #'Result': ['Результаты', 'ᵢ', 'xᵢ', 'i= : 0, n', 'xᵢ четное', 'xᵢ нечетное']
    },
    'Division': {
        'Source': ['Диапазон', '№', 'Начало', 'Конец']
    }
}
