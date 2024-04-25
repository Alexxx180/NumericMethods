from common.commander.input.defaults import *
from common.commander.input.user import *
from menu.tangent.interface.interface import TangentMethod

def TangentEntry(key):
    name = 'Tangent'
    TangentMethod(key, Defaults[name][key] if are_defaults() else Input[name]())

if __name__ == '__main__':
    print("Не реализована")
