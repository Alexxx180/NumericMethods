from common.commander.texts.queries import *
from common.handlers.input.values.list import input_list

Requests = {
    'division': (texts['a'], texts['b'], texts['n'], texts['e']),
    'tangent': (texts['a'], texts['b'], texts['e']),
    'runge': {
        'A': (texts['x'], texts['y'], texts['h'], texts['n']),
        'B': (texts['yd'], texts['a'], texts['b'])
    },
    'simpson': (texts['a'], texts['b'], texts['start'], texts['end'], texts['e'])
}

Input = {
    'Division': (lambda: input_list(Requests['division'], 
        (float, 'a'), (float, 'b'), (validate_e), (lambda: request_n(0, 100)))
    ),
    'Tangent': (lambda: input_list(Requests['tangent'],
        (float, 'a'), (float, 'b'), (validate_e))
    ),
    'Runge': {
        'A': (lambda: input_list(Requests['runge']['A'],
            (float, 'x'), (float, 'y'), (float, 'h'), (int, 'n'))
        ),
        'B': (lambda: input_list(Request['runge']['B'],
            (float, 'yp'), (float, 'a'), (float, 'b'))
        )
    },
    'Simpson': (lambda b: input_list(Requests['Simpson'],
        (float, 'a'), (float, b), (float, 'start'), (float, 'end'), (validate_e))
    ),
}
