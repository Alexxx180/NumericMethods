from common.commander.formula.text import *
from common.commander.defaults import *
from common.commander.input import *
from menu.simpson.interface import SimpsonMethod

def SimpsonFormulaEntry(form):
    if has_form(1, 2, form):
        return

    print(Descriptions['Simpson'][form])

    if are_defaults():
        args = Defaults['Simpson'][form]
        if form != 1:
            args[1] = None
    else:
        args = Input['Simpson']('b' if form == 1 else '')

    SimpsonMethod(args)
