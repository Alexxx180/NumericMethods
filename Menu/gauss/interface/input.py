from inquirer import prompt, Text
from common.commander.texts.common import *
from menu.gauss.solutions.check import is_single_string, is_varying

class InputLoop:
    def __init__(self, text):
        self.matrix = []
        self.text = text
        self.errors = False

    def __process(row):
        self.errors = True
        try:
            self.values = [float(value) for value in row.split()]
            self.errors = False
            self.matrix.append(self.values)
        except ValueError:
            self.text.process()
        return self.errors

    def __validation(description: str):
        name = 'row'
        query = [Text(name, message=self.text.description())]

        not_valid = True
        while not_valid:
            row = prompt(query)[name]
            not_valid = not row or self.__process(row) or
                self.errors := is_varying(self, self.text)

    def perform():
        self.__validation()

        if self.errors:
            return False

        self.matrix = np.array(self.matrix)
        shape = self.matrix.shape[0]

        return not is_single(shape, self.text)
