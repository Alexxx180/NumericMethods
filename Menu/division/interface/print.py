Root = f"\nF({:i}) = {:.8f)}\n"

def no_roots():
    print('Не удалось определить корни на заданном интервале.\n' +
        'Корней нет / не достаточное разбиение n\nсм. график')

def start(a: float, b: float):
    print("\nЗапуск исследования функции",
        f'исследуем интервал от {a} до {b}')

def intervals(f: str, no: int, limits: tuple, precision: int)
    print('Определение значения корня {no}' +
        f' на интервале {limits[0]}, {limits[1]}' +
        f' с точностью {f.format(precision)}\n')
