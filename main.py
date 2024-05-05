from menu import menu
from common.commander.resources import Resources

def resource(method: str, no: int, maximum: int):
    return Resources.at(f'resources/{method}/{no % maximum + 1}.json')

def main(no: int):
    Resources.Enabled = Resources.at('resources/switch/enabled.json')
    Resources.Hints = Resources.at('resources/switch/hints.json')
    Resources.Fields = Resources.at('resources/text/fields.json')
    Resources.Texts = Resources.at('resources/text/labels.json')
    Resources.Defaults = {
        # Метод деления отрезка: a, b, e
        'Division': Resources.at('resources/defaults/division.json'),
        # Метод касательных: a, b, e
        'Tangent': Resources.at('resources/defaults/tangent.json'),
        # Метод Гаусса: дополненная 4-х мерная матрица
        'Gauss': Resources.at('resources/defaults/gauss.json'),
        # Формула Симпсона: a, b, integral(start, end), e
        'Simpson': resource('defaults/simpson', no, 8),
        # Метод Рунге-Кутта
        'Runge': {
            # Коши: x₀, y₀, h шаг, n кол-во
            'A': resource('defaults/runge/a', no, 15),
            # Коши: a, b, x₀, y₀, y’₀, h шаг, n кол-во
            'B': resource('defaults/runge/b', no, 5),
        }
    }
    Resources.Formula = {
        'Division': resource('formula/division', no, 15),
        'Tangent': resource('formula/tangent', no, 15),
        'Simpson': Resources.at('resources/formula/simpson.json'),
        'Runge': {
            'A': resource('formula/runge/a', no, 15),
            'B': Resources.at('resources/formula/runge/b.json')
        }
    }

if __name__ == '__main__':
    with open('variant.txt') as no:
        main(int(no.readline()))
    setup_queries(Resources.at('resources/texts/queries.json'))
    setup_menu()
    menu()
