import menu.gauss.solutions
import menu.gauss.solutions.checks
from menu.gauss.interface.defaults import code_defaults
from menu.handlers.func import pause

def GaussMethod(array):
    if GaussChecks.is_suitable(array.shape):
        method = Gauss(array)
        method.elimination()
    else:
        print("Нет решения")

    pause()

if __name__ == '__main__':
    print("Не реализована")
