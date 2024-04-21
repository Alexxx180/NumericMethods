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
    'a': Text('a', message='Введите a', validate=__number),
    'b': Text('b', message='Введите b', validate=__number),
    'e': Text('e', message='Введите точность e', validate=__number),
    'x': Text('x', message='Введите x₀', validate=__number),
    'y': Text('y', message='Введите y₀', validate=__number),
    'yd': Text('yp', message="Введите y'₀", validate=__number),
    'h': Text('h', message='Введите h', validate=__number),
    'n': Text('n', message='Введите n', validate=__number),
    'start': Text('start', message='Введите начало интегрирования', validate=__number),
    'end': Text('end', message='Введите конец интегрирования', validate=__number)
}

ranges = (Confirm('range_error', message='Конец диапазона меньше его начала.\nПоменять значения местами?\n', default=True))
