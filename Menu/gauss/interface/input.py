import numpy as np
from inquirer import prompt, Text
from menu.gauss.solutions.checks import is_single, is_varying
from menu.gauss.interface.errors import Errors

class InputLoop:
    def __init__(self, text):
        self.text = text
        self.empty = 'empty'
        self.vary = 'vary'
        self.errors = Errors((self.empty, 'invalid', self.vary))

    def __process(self, row) -> bool:
        try:
            self.row = [float(cell) for cell in row.split()]
            self.columns.append(self.row)
            print(self.columns)
            return False
        except ValueError:
            self.text.process()
            return True

    def __validation(self):
        name = 'row'
        query = [Text(name, message=self.text.description())]

        while not self.errors.at[self.empty]:
            print('k')
            row: str = prompt(query)[name]
            self.errors.compute((
                lambda: len(row) == 0,
                lambda: self.__process(row),
                lambda: is_varying(self, self.text)
            ))

    def perform(self):
        self.columns: list = []
        print('j')
        self.__validation()
        print('NOPE')

        if self.errors.at[self.vary] or len(self.columns) == 0:
            print('VERY BAD')
            return False

        self.matrix = np.array(self.columns)
        shape = self.matrix.shape[0]

        return not is_single(shape, self.text)
