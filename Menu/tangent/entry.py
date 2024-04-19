from common.commander.defaults import *
from common.commander.input import *

def Tangent(key):
    name = 'Tangent'
    abe = Defaults[name][key] if are_defaults() else Input[name]
    TangentMethod(key, abe)

if __name__ == '__main__':
    print("Не реализована")
