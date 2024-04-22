from inquirer import List
from menu.division.entry import DivisionEntry
from menu.tangent.entry import TangentEntry
from menu.gauss.entry import GaussEntry
from menu.simpson.entry import SimpsonFormulaEntry
from menu.runge.entry import RungeKuttaEntry

Main = 'option'

start = [List(Main, message="Выбрано",
    choices=(
        'Метод Деления отрезка',
        'Метод касательных',
        'Метод Гауса',
        'Формула Симпсона',
        'Метод Рунге – Кутта',
        'Выход'
    )
)]

options = {
    'sympson': (List('sympson', message="Выбрано", choices=('Формула 1', 'Формула 2'))),
    'tangent': (List('tangent', message="Выбрано", choices=('Формула A', 'Формула B'))),
    'runge': (List('runge', message="Выбрано", choices=('Задание A', 'Задание B')))
}

methods = {
    'Метод Деления отрезка': DivisionEntry,
    'Метод касательных': (TangentEntry, 'tangent',
        {'Формула A': 'A', 'Формула B': 'B'}
    ),
    'Метод Гауса': GaussEntry,
    'Формула Симпсона': (SimpsonFormulaEntry, 'sympson',
        {'Формула 1': 'A', 'Формула 2': 'B'}
    ),
    'Метод Рунге – Кутта': (RungeKuttaEntry, 'runge',
        {'Задание A': 'A', 'Задание B': 'B'}
    )
}
