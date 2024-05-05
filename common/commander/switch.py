from inquirer import prompt, Confirm
from common.commander.resources import Resources

def __number(_, response) -> bool:
    valid = False
    try:
        float(response) ; valid = True
    except ValueError:
        print("Неверный ввод, повторите")
    return valid

def __confirm(name: str, message: str) -> bool:
    return prompt([Confirm(name, message=message, default=True)])[name]

def are_defaults() -> bool:
    return __confirm('confirm', 'Использовать значения по умолчанию?')

def swap_instead_repeat() -> bool:
    return __confirm('confirm', 'Конец меньше начала диапазона.\nПоменять их местами?\n')

def View(control: str, method: str) -> bool:
    confirm = [Confirm('c', message=Resources.Texts[control][method], default=True)]
    return Resources.Enabled[control][method] or prompt(confirm)['c']

def setup_input(queries: dict):
    q: dict = {}
    for argument, message in queries.items():
        q[argument] = Text(argument, message=message, validate=__number)

    division = (q['a'], q['b'], q['n'], q['e'])
    tangent = (q['a'], q['b'], q['e'])
    simpson = (q['a'], q['b'], q['start'], q['end'], q['e'])
    runge = {
        'A': (q['x'], q['y'], q['h'], q['n']),
        'B': (q['a'], q['b'], q['x'], q['y'], q['yd'], q['h'])
    }
    Resources.Input = {
        'Division': lambda: input_list(division, (float, ('a', 'b')), validate_e, lambda: request_n(0, 100))
        'Tangent': lambda: input_list(tangent, (float, ('a', 'b')), validate_e),
        'Simpson': lambda b: input_list(simpson, (float, ('a', b)), lambda: pair(float, 'start', 'end'), validate_e)
        'Runge': {
            'A': lambda: input_list(runge['A'], (float, ('x', 'y', 'h')), (int, 'n')),
            'B': lambda: input_list(runge['B'], (float, ('a', 'b', 'x', 'y', 'y’', 'h')), (int, 'n'))
        }
    }
