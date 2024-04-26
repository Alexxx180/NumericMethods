from common.commander.formula.text import *
from common.commander.input.defaults import *
from common.commander.input.user import *
from menu.simpson.interface.interface import SimpsonInterface

def SimpsonFormulaEntry(form: str):
    print(Descriptions['Simpson'][form])

    if are_defaults():
        args = Defaults['Simpson'][form]
    else:
        args = Input['Simpson']('b' if form == 'B' else '')

    SimpsonInterface(args, form).start()
