import numpy as np
from common.drawing import Table
from common.commander.formula.text import *
from common.commander.defaults import *
from common.commander.input import *
from menu.gauss.interface import GaussMethod

def GaussEntry():
    array = np.array(Defaults['Gauss'], dtype=float)
    Table([""], "Исходная матрица").matrix(array).show()

    if are_defaults():
        GaussMethod(array)
        return

    validator = InputLoop()
    if validator.perform():
        GaussMethod(validator.matrix)
