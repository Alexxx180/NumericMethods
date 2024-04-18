import inquirer
import numpy as np
from Classes.Table import Table
from menu.gauss.interface import GaussMethod
from menu.gauss.interface.defaults import real_defaults

def GaussEntry():
    array = np.array(real_defaults(), dtype=float)
    Table([""], "Исходная матрица").matrix(array).show()

    name = 'question'
    defaults = 'Использовать матрицу?'
    question = [inquirer.Confirm(name, message=defaults, default=True)] 
    question = inquirer.prompt(question)

    if question[name]:
        GaussMethod(array)
        return

    validator = InputLoop()
    if validator.perform():
        GaussMethod(validator.matrix)
