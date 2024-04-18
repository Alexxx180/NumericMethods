import common.texts.queries as q
from common.input.list import input_list

Input = {
    'Division': (lambda: input_list(q.division_request, 
        (float, 'variable_a'), (float, 'variable_b')
        (validate_e), (lambda: reques_n(0, 100)))
    ),
    'Runge': {
        'A': (lambda: input_list(query.x_y_h_n_request,
            (float, 'variable_x'), (float, 'variable_y'),
            (float, 'variable_h'), (int, 'variable_n'))
        ),
        'B': (lambda: input_list(query.yp_a_b_request,
            (float, 'variable_yp'),
            (float, 'variable_a'),
            (float, 'variable_b'))
        )
    },
    'Simpson': (lambda variable_b: input_list(
        q.simpson_request, (float, 'variable_a'), (float, variable_b),
        (float, 'variable_start'), (float, 'variable_end'), (validate_e)
    ),
}
