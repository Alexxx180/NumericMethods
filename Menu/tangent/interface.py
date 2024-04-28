from common.commander.texts.common import *
from common.flow.canvas.tangent import canvas_from
from menu.tangent.solutions.functions import tangent, draw
from menu.tangent.solutions.research import Research

def TangentMethod(key: str, name: str, args: tuple):
    research = Research(key, name)
    research.start(args)

    derive = research.derives[0]
    message = research.message

    canvas = canvas_from(key, name, derive, args)

    text = Text(name)
    text.message(message)

    if research.roots is None:
        text.no_roots(args[0], args[1])
        return

    rows = tangent(args[2], research)
    orders = draw(rows, name, 100)

    text.result(message, rows)
    canvas.show(orders)
    text.pause()
