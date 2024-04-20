def formatting(string: str, iterable):
    return [string.format(num) for num in iterable]

Variables = {
    'Simpson': "a = {0}, b = {1}, e = {2:.15f}, h = {3}, M = {4}, n = {5}\n" +
        "Пределы интегрирования {6}..{7}\nЗначение интеграла = {8}"
}
