from common.commander.resources import Resources
from common.handlers.interaction import pause
from common.handlers.input.validate import list_argument

def __pass_argument(parameters: list, convert: callable, args):
    if isinstance(args, str):
        list_argument(parameters, convert, name)
        return

    for name in args:
        while not list_argument(parameters, convert, name):
            pause(Resources.Texts['Common']['Input'])

def listing(*args):
    parameters: list = []

    for arg in args:
        if isinstance(arg, callable):
            parameters.append(arg())
        elif len(arg) == 2:
            __pass_argument(parameters, arg[0], arg[1])

    return parameters
