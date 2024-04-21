from menu.tangent.interface.plots import TangentInterface
from menu.tangent.solutions.functions.formula import TangentFormula
from menu.tangent.solutions.functions import tangent
from menu.tangent.solutions.research import Research

def TangentMethod(key: str, args: tuple):
    name = 'Tangent'
    task = Formula[name][key]

    research = Research(task)
    research.start(args)

    message: str = research.message

    view = TangentPlots(name, 100, args, task)
    print(Texts[name]['Message'].format(message))

    if research.roots is not None:
        row = tangent(args[2], research)
        view.draw(row)
        Table(Tangent[name]['Result'], message).row(row).show().pause()
    else:
        pause(Texts[name]['No roots'].format(args[0], args[1]))
