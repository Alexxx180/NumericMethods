from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.simpson.interface import SimpsonInterface

def SimpsonFormulaEntry(form: str):
    name = 'Simpson'

    if are_defaults():
        args = Resources.Defaults[name][form]
    else:
        args = Resources.Input[name]('b' if form == 'B' else '')

    SimpsonInterface(args, name, form).start()
