from Division_segment.main import Division_segment  # noqa: E402
from Classes.Input import vinput, validate_e
from Menu.common import request_a_b, request_n
import Classes.Texts.Queries as q

# Начало   a, b, n, e
def Division_defaults():
    return 1, 2, 7, 0.01

def Division():
    if vinput(q.confirm)['confirm']:
        a, b, n, e = Division_defaults()
    else:
        a, b = request_a_b()
        e = validate_e()
        n = request_n(0, 100)

    ic(a, b, n, e)  # noqa: F821
    # Применение метода
    Division_segment(a, b, n, e)
