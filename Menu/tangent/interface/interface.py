from menu.tangent.interface.plots import TangentPlots
from menu.tangent.solutions.functions import tangent
from menu.tangent.solutions.research import Research

def TangentMethod(key: str, args: tuple):
    name = 'Tangent'

    research = Research(key, name)
    research.start(args)

    message: str = research.message

    view = TangentPlots(key, name, 100, args, task)
    print(Texts[name]['Message'].format(message))

    if research.roots is not None:
        row = tangent(args[2], research)
        view.draw(row)
        Table(Tangent[name]['Result'], message).row(row).show().pause()
    else:
        pause(Texts[name]['No roots'].format(args[0], args[1]))
