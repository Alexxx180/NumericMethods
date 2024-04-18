import inquirer

# Валидация ввода номера для запросов
def validate_number(_, response):
    try:
        float(response)
        return True
    except ValueError:
        print("Неверный ввод\nПовторите")
        return False

a_b_request = [
    inquirer.Text('variable_a', message='Введите a', validate=validate_number),
    inquirer.Text('variable_b', message='Введите b', validate=validate_number)]

stat_end_a_b_request = [
    inquirer.Text('variable_start',
        message='Введите начало интегрирования',
        validate=validate_number),
    inquirer.Text('variable_end',
        message='Введите конец интегрирования',
        validate=validate_number)]

e_request = [inquirer.Text('variable_e',
    message='Введите точность e', validate=validate_number)]

n_request = [inquirer.Text('variable_n',
    message='Введите число разбиений n для исследования функции',
    validate=validate_number)]

x_y_h_n_request =[
    inquirer.Text('variable_x', message='Введите x₀', validate=validate_number),
    inquirer.Text('variable_y', message='Введите y₀', validate=validate_number),
    inquirer.Text('variable_h', message='Введите h', validate=validate_number),
    inquirer.Text('variable_n', message='Введите n', validate=validate_number)]

yp_a_b_request =[
    inquirer.Text('variable_yp', message="Введите y'₀", validate=validate_number),
    inquirer.Text('variable_a', message='Введите a', validate=validate_number),
    inquirer.Text('variable_b', message='Введите b', validate=validate_number)]

range_error = [
    inquirer.Confirm('range_error',
    message='Конец отрезка b не может быть меньше начала отрезка' +
        ' a.\nДолжно быть a < b, b > a\nПоменять a и b местами?\n',
    default=True)]

e_s_error = [
    inquirer.Confirm('e_s_error',
    message='Начало интегрирования больше конца ' +
        'интегрирования.\nПоменять start и end местами?\n',
    default=True)]

confirm = [
    inquirer.Confirm('confirm', message='Использовать значения по умолчанию?',
    default=True)]
