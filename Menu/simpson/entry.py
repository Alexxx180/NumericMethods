from common.commander.formula.text import *
from common.commander.defaults import *
from common.commander.input import *
from menu.simpson.interface import SimpsonMethod

def SimpsonFormulaEntry(form: str):
    print(Descriptions['Simpson'][form])

    if are_defaults():
        args = Defaults['Simpson'][form]
    else:
        args = Input['Simpson']('b' if form == 'B' else '')

    SimpsonMethod(args)
