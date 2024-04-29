import numpy as np
from common.commander.input.defaults import *
from common.commander.input.user import *
from common.commander.texts.fields import *
from common.flow.texts.gauss import Text
from menu.gauss.interface.interface import GaussMethod

def GaussEntry():
    name = 'Gauss'
    array = np.array(Defaults[name], dtype=float)

    text = Text(name)
    text.source(array)

    if are_defaults():
        GaussMethod(array, text)
    else:
        validator = InputLoop(text)
        if validator.perform():
            GaussMethod(validator.matrix, validator.text)
    text.pause()
