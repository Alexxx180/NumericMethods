from common.commander.switch import are_defaults
from common.commander.resources import Resources
from menu.runge.interface import RungeKuttaTasks

def RungeKuttaEntry(form: str):
    name = 'Runge'

    if are_defaults():
        args = Resources.Defaults[name][form]
    else:
        args = Resources.Input[name][form]()

    implementation = RungeKuttaTasks(name, form, args)
    implementation.method()
