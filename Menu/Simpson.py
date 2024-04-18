from Simpson_formula.Simpson import Simpson
from Formulas import simpson_f
from Classes.Input import vinput, validate_e
import Classes.Texts.Queries as q

def Simpson_formula(form):
    form1 = form == 1
    if (not form1) and form != 2:
        return

    simpson_f(form)

    if are_defaults():
        args = defaults(form)
        if not form1:
            args[1] = None
    else:
        args = inputAorB('variable_b' if form1 else '')

    SimpsonMethod(args)
