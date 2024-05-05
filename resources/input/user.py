from common.commander.texts.queries import *
from common.handlers.input.values.list import input_list

Requests = {
    'division': (q['a'], q['b'], q['n'], q['e']),
    'tangent': (q['a'], q['b'], q['e']),
    'runge': {
        'A': (q['x'], q['y'], q['h'], q['n']),
        'B': (q['a'], q['b'], q['x'], q['y'], q['yd'], q['h'])
    },
    'simpson': (q['a'], q['b'], q['start'], q['end'], q['e'])
}

Input = {
    'Division': (lambda: input_list(Requests['division'], 
        (float, 'a'), (float, 'b'), validate_e, lambda: request_n(0, 100))
    ),
    'Tangent': (lambda: input_list(Requests['tangent'],
        (float, 'a'), (float, 'b'), validate_e)
    ),
    'Runge': {
        'A': (lambda: input_list(Requests['runge']['A'],
            (float, 'x'), (float, 'y'), (float, 'h'), (int, 'n'))
        ),
        'B': (lambda: input_list(Request['runge']['B'],
            (float, 'a'), (float, 'b'), (float, 'x'), (float, '')
            (float, 'yp'), ()
            )
        )
    },
    'Simpson': (lambda b: input_list(Requests['Simpson'],
        (float, 'a'), (float, b), (float, 'start'), (float, 'end'), (validate_e))
    ),
}
