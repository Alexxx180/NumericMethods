import common.texts.queries as q
from inquirer import prompt
from common.commander.switch import swap_instead_repeat
from common.handlers.validate import specify, number

errors = Printer('Common').act(print)

def validate_e() -> float:
    arg: tuple = ('e', 0.0)
    check: callable = lambda e: not e[0] or abs(e[1]) >= 1 or e[1] < 1e-15 or e[1] == arg[1]
    return specify(check, arg, 'Wrong e')

def request_n(start: int, end: int) -> float:
    arg = ('n', 0)
    check: callable = lambda n: not n[0] or n[1] < start or n[1] > end
    return specify(check, arg, 'Wrong n', start, end)

def pair(convert: callable, start: str, end: str):
    query: callable = lambda name: convert(prompt(Resources.Queries[name])[name])
    a, b = query(start), query(end)

    while b < a:
        if swap_instead_repeat():
            a, b = b, a
        else:
            a, b = query(start), query(end)

    return (a, b)

def setup_input(queries: dict):
    for argument, message in queries.items():
        Resources.Queries[argument] = [Text(argument, message=message, validate=number)]

    Resources.Input = {
        'Division': lambda: listing((float, ('a', 'b')), validate_e, lambda: request_n(0, 100))
        'Tangent': lambda: listing((float, ('a', 'b')), validate_e),
        'Simpson': lambda b: listing((float, ('a', b)), lambda: pair(float, 'ₐ', 'ᵇ'), validate_e)
        'Runge': {
            'A': lambda: listing((float, ('x', 'y', 'h')), (int, 'n')),
            'B': lambda: listing((float, ('a', 'b', 'x', 'y', 'y’', 'h')), (int, 'n'))
        }
    }
