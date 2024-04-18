from menu.tangent.interface.plots import TangentInterface
from menu.tangent.solutions.functions.formula import TangentFormula
from menu.tangent.solutions.functions import tangent
from menu.tangent.solutions.research import Research

def TangentMethod(name: str, abe: tuple):
    research = Research(Formula['Tangent'][name])
    research.start(abe)

    view = TangentInterface(name, 100)
    view.memorize(name, research.message)

    if research.roots is not None:
        view.DrawTangent(tangent(abe[2], research))
    else:
        view.no_roots(abe[0], abe[1])

    view.show_graph()
