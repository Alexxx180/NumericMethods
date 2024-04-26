from common.commander.texts.common import *
from common.commander.texts.fields import *
from common.handlers.interaction import pause
from common.handlers.printer import Printer
from menu.tangent.interface.canvas import canvas_from
from menu.tangent.solutions.functions import tangent, draw
from menu.tangent.solutions.research import Research

def TangentMethod(key: str, name: str, args: tuple):
    research = Research(key, name)
    research.start(args)

    canvas = canvas_from(key, name, research.derives[0], args)

    text = Printer(name)
    text.add(print, 'Message', research.message)

    if research.roots is not None:
        row = tangent(args[2], research)
        orders = draw(row, name, 100)
        canvas.show(orders)
        grid((name, 'Result'), row, research.message)
        text.print().clear()
    else:
        text.add(pause, 'No roots', args[0], args[1]).print().clear()
