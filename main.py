from menu import menu
from common.commander.resources import Resources

def resource(method: str, no: int, maximum: int):
    return Resources.at(f'resources/{method}/{no % maximum + 1}.json')

def main(no: int):
    Resources.Enabled = Resources.at(f'resources/switch/enabled.json')
    Resources.Queries = Resources.at(f'resources/switch/queries.json')
    Resources.Fields = Resources.at(f'resources/text/fields.json')
    Resources.Texts = Resources.at(f'resources/text/labels.json')

    Resources.Defaults = {
        'Division': Resources.at(f'resources/defaults/division.json'),
        'Tangent': Resources.at(f'resources/defaults/tangent.json'),
        'Gauss': Resources.at(f'resources/defaults/gauss.json'),
        'Simpson': resource('defaults/simpson', no, 8),
        'Runge': {
            'A': resource('defaults/runge/a', no, 15),
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
    menu()
