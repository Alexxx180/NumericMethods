from menu.handlers.func import pause

class SegmentPrint:
    NoRoots = 'Не удалось определить корни на заданном интервале.\nКорней нет / не достаточное разбиение n\nсм. график'
    Root = f"\nF({:i}) = {:.8f)}\n"

    @staticmethod
    def start(a: float, b: float):
        print("\nЗапуск исследования функции",
            f'исследуем интервал от {a} до {b}')

    @staticmethod
    def intervals(f: str, no: int, limits: tuple, precision: int)
        print('Определение значения корня {no}' +
            f' на интервале {limits[0]}, {limits[1]}' +
            f' с точностью {f.format(precision)}\n')
