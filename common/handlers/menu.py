from common.handlers.interaction import ask
from menu.division.entry import DivisionEntry
from menu.tangent.entry import TangentEntry
from menu.gauss.entry import GaussEntry
from menu.simpson.entry import SimpsonFormulaEntry
from menu.runge.entry import RungeKuttaEntry

def select(query: str, choices: dict, options: dict):
    invoke = {
        'division': DivisionEntry,
        'tangent': TangentEntry,
        'gauss': GaussEntry,
        'simpson': SimpsonFormulaEntry,
        'runge': RungeKuttaEntry
    }

    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke[query](value)
