from common.commander.input.defaults import *
from common.commander.input.user import *
from menu.runge.interface import RungeKuttaTasks

def RungeKuttaEntry(form: str):
    name = 'Runge'
    args = Defaults[name][form] if are_defaults() else Input[name][form]

    implementation = RungeKuttaTasks(name, form, args)
    implementation.method()
