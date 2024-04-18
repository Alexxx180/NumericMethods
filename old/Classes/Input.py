import inquirer
import Classes.Texts.Queries as q

# Клавиши выбора
yes = { 'y', 'Y', 'н', 'Н' }
no = { 'n', 'N', 'т', 'Т' }

# Проверка ввода да-нет
def UserQuery(query):
    print(query)
    user = input() ; ic(user) # noqa: F821
    accept = user in yes
    decline = user in no
    return accept, decline

# Выбор Да-Нет
def UserSelect(query):
    accept, decline = UserQuery(query)

    while not (accept or decline):
        accept, decline = UserQuery(query)

    return accept

# Ввод переменных
def vinput(query):
    return inquirer.prompt(query)

# Ввод 'e'
def validate_e():
    name = 'variable_e'
    e = float(vinput(q.e_request)[name])

    while abs(e) >= 1 or e < 0.000000000000001 or e == 0:
        message = ('e: требуется e < 1, e > -1, ' +
            'e ≠ 0. e: не должно быть > 15 ' +
            'десятичных знаков\nПовторите')
        print(message)
        request = inquirer.prompt(e_request)
        e = float(query)

    return e

# Подмена диапазонов
def swap_ranges(error, v_request, variables):
    if error:
        return b, a
    else:
        query = vinput(v_request)
        a = float(query[variables[0]])
        b = float(query[variables[1]])
        return a, b

# Валидация переменных-диапазонов
def vranges(v_request, variables, error_query, error_name):
    query = vinput(v_request)
    start = float(query[variables[0]])
    end = float(query[variables[1]])

    while end < start:
        error = vinput(error_query)[error_name]
        start, end = swap_ranges(error, v_request, variables)

    return start, end

# Валидация одной переменной в диапазоне
def vrange(request, task, start, end):
    n = float(request())

    while n <= start or n > end:
        print(f'{task} должно быть от {start} до {end}\nПовторите')
        n = float(request())

    return n

# Введение списка значений пользователем
def input_list(query, variables):
    result = []
    request = vinput(query)
    for variable in variables:
        convert = variable[0]
        name = variable[1]
        result.append(convert(request[name]))
    return result

def has_form(start: int, count: int, form: int)
    for i in range(start, count):
        if i == form:
            return True
    return False


