import platform

from icecream import install
from os import system
from msvcrt import kbhit, getch
import inquirer

from Menu.Division import Division
from Menu.Tangent import Tangent
from Menu.Gaus import Gaus
from Menu.Simpson import Simpson_formula
from Menu.Runge import runge_kutta
from Formulas import tanden_formula_a, tanden_formula_b, division_formula, simpson_f, Runge_Kutta_f

install()  # Установка ic, чтобы работал везде без доп импорта.
# P.S. ic - это тула для дебага и вывода переменных

def clear():
    if platform.system() == "Windows":
        ic()  # noqa: F821
        while kbhit():
            getch()
        system('cls')
    else:
        system('clear') ; ic()  # noqa: F821


# Проверка можно ли преобразовать
start_menu = [inquirer.List('menu_option', message="Выбрано",
    choices=[
        'Метод Деления отрезка',
        'Метод касательных',
        'Метод Гауса',
        'Формула Симпсона',
        'Метод Рунге – Кутта',
        'Выход'
])]

sympsom_menu = [inquirer.List('sympsom_menu', message="Выбрано",
    choices=['Формула 1', 'Формула 2'],
)]

tangent_menu = [inquirer.List('tangent_menu', message="Выбрано",
        choices=['Формула A', 'Формула B'],
)]

Runge_Kutta_menu = [inquirer.List('Runge_Kutta_menu', message="Выбрано",
        choices=['Задание A', 'Задание B'],
)]


def menu():
    clear() ; ic.disable()  # noqa: F821
    answers = inquirer.prompt(start_menu)
    clear()
    while answers['menu_option'] != 'Выход':
        # answers = inquirer.prompt(start_menu)

        if answers['menu_option'] == 'Метод Деления отрезка':
            division_formula() ; ic()  # noqa: F821
            Division()

        elif answers['menu_option'] == 'Метод касательных':
            answers = inquirer.prompt(tangent_menu)
            clear()
            if answers['tangent_menu'] == 'Формула A':
                tanden_formula_a() ; Tangent("a")
            elif answers['tangent_menu'] == 'Формула B':
                tanden_formula_b() ; Tangent("b")

        elif answers['menu_option'] == 'Метод Гауса':
            Gaus()

        elif answers['menu_option'] == 'Формула Симпсона':
            simpson_f(0)
            answers = inquirer.prompt(sympsom_menu)
            clear()
            if answers['sympsom_menu'] == 'Формула 1':
                Simpson_formula(1)
            elif answers['sympsom_menu'] == 'Формула 2':
                Simpson_formula(2)

        elif answers['menu_option'] == 'Метод Рунге – Кутта':
            answers = inquirer.prompt(Runge_Kutta_menu)
            clear()
            if answers['Runge_Kutta_menu'] == 'Задание A':
                Runge_Kutta_f(1) ; runge_kutta(1)
            elif answers['Runge_Kutta_menu'] == 'Задание B':
                Runge_Kutta_f(2) ; runge_kutta(2)
        clear()
        answers = inquirer.prompt(start_menu)
        clear()
    print("Завершение работы.")


if __name__ == '__main__':
    ic()  # noqa: F821
    menu()
