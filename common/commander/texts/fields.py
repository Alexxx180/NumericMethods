from common.drawing.table.table import Table

a = chr(8776) # Approximation Symbol ≈

Fields = {
    'Runge': {
        'A': {
            'Source': ['Условия', 'x₀', 'y₀', 'h', 'n'],
            'Result': ['Задание А', 'ᵢ', 'x', f'y {a}', 'yₐₙ =', 'yₚᵣ = ']
        },
        'B': {
            'Source': ['Условия', 'x₀', 'y₀', "y'₀", 'a', 'b', 'h', 'n'],
            'Result': ['Задание B', 'i', 'x', f'y {a}', f"y' {a}", f"y'' {a}", "y'' - ay' - by", 'f(x)', 'погрешность'],
            'Functions': ['sin(x)', 'e⁻ˣ', 'cos(x)']
        }
    },
    'Gauss' : {
        'Source': ["Исходная матрица", ""]
    },
    'Tangent' : {
        'Result': ['Результаты вычислений представлены в следующей таблице:',
            'ᵢ', 'x', 'F(xᵢ)', "F'(xᵢ)", '|F(xᵢ)| / m']
    },
    'Simpson' : {
        'Result': ['Результаты', 'ᵢ', 'xᵢ', 'i= : 0, n', 'xᵢ четное', 'xᵢ нечетное']
    },
    'Division': {
        'Source': ['Интервалы с корнями', 'i', 'Диапазон'],
        'Result': ['Найденные корни', 'i', 'Диапазон', 'Корень']
    }
}
