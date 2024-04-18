from inquirer import Text, Confirm

# Валидация ввода номера для запросов
def __number(_, response):
    try:
        float(response)
        return True
    except ValueError:
        print("Неверный ввод\nПовторите")
        return False

a_b_request = [
    Text('variable_a', message='Введите a', validate=__number),
    Text('variable_b', message='Введите b', validate=__number)]

stat_end_a_b_request = [
    Text('variable_start', message='Введите начало интегрирования', validate=__number),
    Text('variable_end', message='Введите конец интегрирования', validate=__number)]

e_request = [Text('variable_e', message='Введите точность e', validate=__number)]

n_request = [Text('variable_n',
    message='Введите число разбиений n для исследования функции',
    validate=__number)]

x_y_h_n_request =[
    Text('variable_x', message='Введите x₀', validate=__number),
    Text('variable_y', message='Введите y₀', validate=__number),
    Text('variable_h', message='Введите h', validate=__number),
    Text('variable_n', message='Введите n', validate=__number)]

yp_a_b_request =[
    Text('variable_yp', message="Введите y'₀", validate=__number),
    Text('variable_a', message='Введите a', validate=__number),
    Text('variable_b', message='Введите b', validate=__number)]

range_error = [
    Confirm('range_error', message='Конец b меньше начала отрезка a.' +
        '\nДолжно быть a < b\nПоменять a и b местами?\n',
    default=True)]

e_s_error = [
    Confirm('e_s_error',
    message='Начало больше конца интегрирования.' +
        '\nПоменять start и end местами?\n',
    default=True)]

confirm = [
    Confirm('confirm', message='Использовать значения по умолчанию?',
    default=True)]
