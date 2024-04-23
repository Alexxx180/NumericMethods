from menu.gauss.solutions.solutions import Gauss
from menu.gauss.solutions.checks import is_suitable
from common.handlers.interaction import pause
from common.commander.texts.common import *

def GaussMethod(array):
    if is_suitable(array.shape):
        Gauss(array).system_elimination()
    else:
        print(Texts['Gauss']['Solutions']['Not found'])
    pause()
