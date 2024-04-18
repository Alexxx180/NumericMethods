import common.texts.queries as q
from common.input.values.single import vinput
from inquirer import prompt

# Ввод 'e'
def validate_e():
    name = 'variable_e'
    request = q.e_request
    e = float(vinput(request)[name])

    while abs(e) >= 1 or e < 0.000000000000001 or e == 0:
        print('e: требуется -1 < e < 1, e ≠ 0. ' +
            'e: не должно быть > 15 десятичных знаков\nПовторите')
        request = prompt(request)
        e = float(query)

    return e

# Проверка наличия формы в программе
def has_form(start: int, count: int, form: int)
    for i in range(start, count):
        if i == form:
            return True
    return False
