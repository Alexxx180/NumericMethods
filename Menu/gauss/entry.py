import numpy as np
from common.drawing.table.table import Table
from common.commander.formula.text import *
from common.commander.input.defaults import *
from common.commander.input.user import *
from common.commander.texts.fields import *
from menu.gauss.interface.interface import GaussMethod

def GaussEntry():
    array = np.array(Defaults['Gauss'], dtype=float)
    Table(Gauss['Source']).matrix(array).show()

    if are_defaults():
        GaussMethod(array)
    else:
        validator = InputLoop()
        if validator.perform():
            GaussMethod(validator.matrix)
