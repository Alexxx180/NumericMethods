from inquirer import Text, Confirm

# Валидация ввода номера для запросов
def __number(_, response):
    try:
        float(response)
        return True
    except ValueError:
        print("Неверный ввод\nПовторите")
        return False

texts = {
    'a': Text('variable_a', message='Введите a', validate=__number),
    'b': Text('variable_b', message='Введите b', validate=__number),
    'e': Text('variable_e', message='Введите точность e', validate=__number),
    'x': Text('variable_x', message='Введите x₀', validate=__number),
    'y': Text('variable_y', message='Введите y₀', validate=__number),
    'yd': Text('variable_yp', message="Введите y'₀", validate=__number),
    'h': Text('variable_h', message='Введите h', validate=__number),
    'n': Text('variable_n', message='Введите n', validate=__number)
    'start': Text('variable_start', message='Введите начало интегрирования', validate=__number),
    'end': Text('variable_end', message='Введите конец интегрирования', validate=__number)
}

Requests = {
    'division': (texts['a'], texts['b'], texts['n'], texts['e']),
    'tangent': (texts['a'], texts['b'], texts['e']),
    'runge': {
        'A': (texts['x'], texts['y'], texts['h'], texts['n']),
        'B': (texts['yd'], texts['a'], texts['b'])
    }
    'simpson': (texts['a'], texts['b'], texts['start'], texts['end'], texts['e'])
}

range_error = [
    Confirm('range_error', message='Конец диапазона меньше его начала.' +
        '\nПоменять значения местами?\n',
    default=True)]
