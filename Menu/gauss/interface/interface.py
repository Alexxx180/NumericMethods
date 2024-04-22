import menu.gauss.solutions.solutions
from menu.gauss.solutions.checks import is_suitable
from common.handlers.interaction import pause
from common.commander.texts.common import *

def GaussMethod(array):
    if is_suitable(array.shape):
        method = Gauss(array)
        method.system_elimination()
    else:
        print(Texts['Gauss']['Solutions']['Not found'])
    pause()
