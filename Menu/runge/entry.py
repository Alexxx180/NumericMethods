import menu.runge.interface
from menu.runge.interface.defaults import defaultsA, defaultsB, are_defaults, inputA, inputB
from Class.Input import has_form

def RungeKuttaEntry(form):
    if not has_form(1, 2, form):
        return

    defaults = are_defaults()
    args1 = defaultsA(form) if defaults else inputA()

    # Применение методов A или B
    if form == 1:
        implementation = RungeKuttaTasks(args1)
    else:
        args2 = defaultsB() if defaults else inputB()
        implementation = RungeKuttaTasks(args1, args2)

    implementation.method()
