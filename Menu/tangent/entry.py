from menu.tangent.interface import TangentInterface
from menu.tangent.solutions.functions.formula import TangentFormula
from menu.tangent.solutions.functions import tangent
from menu.tangent.solutions.research import Research

def TangentMethod(name: str, abe: tuple):
    formula = TangentFormula(name)
    research = Research(formula.task)
    research.start(abe)

    view = TangentInterface(name, 100)
    view.memorize(name, research.message)

    if research.roots is not None:
        row = tangent(abe[2], research)
        DrawTangent(row, view)
    else:
        view.no_roots(abe[0], abe[1])

    view.show_graph()

if __name__ == '__main__':
    print("Не реализована")
