import menu.gauss.solutions
import menu.gauss.solutions.checks
from menu.gauss.interface.defaults import code_defaults
from menu.handlers.func import pause

def GaussMethod(array):
    array = code_defaults(array)

    if GaussianChecks.is_suitable(array.shape):
        method = Gauss(array)
        x = method.elimination()
        if x is not None:
            print("", x)
    else:
        print("Нет решения")

    pause()

if __name__ == '__main__':
    print("Не реализована")
