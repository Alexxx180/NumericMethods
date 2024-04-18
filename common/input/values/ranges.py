from common.input.common import vinput

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
