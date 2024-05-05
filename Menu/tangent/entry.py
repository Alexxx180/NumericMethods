from common.commander.switch import are_defaults
from common.commander.Resource import Resource
from menu.tangent.interface import TangentMethod

def TangentEntry(key):
    name = 'Tangent'

    if are_defaults():
        args = Defaults[name][key]
    else:
        args = Input[name]()

    TangentMethod(key, name, args)
