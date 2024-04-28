from common.commander.formula.text import *
from common.commander.input.defaults import *
from common.commander.input.user import *
from menu.simpson.interface import SimpsonInterface

def SimpsonFormulaEntry(form: str):
    #print(Descriptions['Simpson'][form])
    name = 'Simpson'

    if are_defaults():
        args = Defaults[name][form]
    else:
        args = Input[name]('b' if form == 'B' else '')

    SimpsonInterface(args, name, form).start()
