from inquirer import prompt, Text
from common.commander.texts.common import *
from menu.gauss.solutions.check import is_single_string, is_varying

class InputLoop:
    def __init__(self):
        self.matrix = []

    def process(row):
        self.errors = True
        try:
            self.values = [float(value) for value in row.split()]
            self.errors = False
            self.matrix.append(self.values)
        except ValueError:
            pause(Texts['Gauss']['Input']['Data'])
        return self.errors

    def loop(description: str):
        name = 'row'
        row = prompt([Text(name, message=description)])[name]
        return not (not row or process(row) or self.errors = is_varying(self))

    def perform():
        description = Texts['Gauss']['Input']['String']
        self.errors = False
        while validating = loop(description):
            pass

        if self.errors:
            return False

        self.matrix = np.array(self.matrix)
        return not is_single_string(self.matrix.shape[0]):
