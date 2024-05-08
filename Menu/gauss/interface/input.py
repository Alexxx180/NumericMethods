import numpy as np
from inquirer import prompt, Text
from menu.gauss.solutions.checks import is_single, is_varying

class InputLoop:
    def __init__(self, text):
        self.matrix = []
        self.text = text
        self.errors = False

    def __process(self, row):
        self.errors = True
        try:
            self.values = [float(value) for value in row.split()]
            self.errors = False
            self.matrix.append(self.values)
        except ValueError:
            self.text.process()
        return self.errors

    def __check(self, row, text) -> bool:
        not_valid = not row or self.__process(row)
        if not_valid: self.errors = is_varying(self, text)
        return not_valid or self.errors

    def __validation(self):
        name = 'row'
        query = [Text(name, message=self.text.description())]

        not_valid = True
        while not_valid:
            row = prompt(query)[name]
            not_valid = self.__check(row, self.text)

    def perform(self):
        self.__validation()

        if self.errors:
            return False

        self.matrix = np.array(self.matrix)
        shape = self.matrix.shape[0]

        return not is_single(shape, self.text)
