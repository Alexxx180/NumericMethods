from Tangent_method.main import Tangent_method_a, Tangent_method_b  # noqa: E402
from Classes.Input import vinput, validate_e
from Menu.common import request_a_b
import Classes.Texts.Queries as q

# Начало         a,   b, e
def Tangent_defaults(key):
    defaults = {
        'a' : [  1, 1.2, 0.000001],
        'b' : [0.3, 0.7, 0.000001]
    }
    return defaults[key]

def Tangent(key):
    if vinput(q.confirm)['confirm']:
        abe = defaults(key)
    else:
        a, b = request_a_b()
        e = validate_e()
        abe = (a, b, e)

    TangentMethod(key, abe)
