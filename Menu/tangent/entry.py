from common.commander.defaults import *
from common.commander.input import *

def Tangent(key):
    name = 'Tangent'
    TangentMethod(key, Defaults[name][key] if are_defaults() else Input[name]())

if __name__ == '__main__':
    print("Не реализована")
