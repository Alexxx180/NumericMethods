def formatting(string, iterable):
    return [string.format(num) for num in iterable]

def init_args(params: tuple, arguments: list):
    args = {}
    for i in range(0, len(params)):
        args[params[i]] = arguments[i]
    return args
