from common.commander.input.defaults import *
from common.commander.input.user import *

def TangentEntry(key):
    name = 'Tangent'
    TangentMethod(key, Defaults[name][key] if are_defaults() else Input[name]())

if __name__ == '__main__':
    print("Не реализована")
