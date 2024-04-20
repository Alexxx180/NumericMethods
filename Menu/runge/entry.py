from common.commander.formula.text import *
from common.commander.defaults import *
from common.commander.input import *
from menu.runge.interface import RungeKuttaTasks

def RungeKuttaEntry(form):
    defaults = are_defaults()
    args1 = Defaults['Runge']['A'][form] if defaults else Input['Runge']['A']

    if form == 1:
        implementation = RungeKuttaTasks(args1)
    else:
        args2 = Defaults['Runge']['B'] if defaults else Input['Runge']['B']
        implementation = RungeKuttaTasks(args1, args2)

    implementation.method()
