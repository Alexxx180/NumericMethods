import inquirer
from menu.gauss.solutions.check import is_single_string, is_varying

class InputLoop:
    Name = 'row'

    def __init__(self):
        self.values = None
        self.matrix = []

    def process_input_string(row):
        self.errors = True
        try:
            self.values = [float(value) for value in row.split()]
            self.errors = False
        except ValueError:
            pause("Неверный ввод")
        return self.errors

    def loop(description: str):
        row_input = inquirer.prompt([inquirer.Text(Name, message=description)])
        row = row_input[Name]

        if not row:
            return False

        if process_input_string(row):
            return False

        self.matrix.append(self.values)

        if self.errors = is_varying(self.values, self.matrix):
            return False

        return True

    def perform():
        description = 'Введите строку матрицы / пустую строку для завершения'
        self.errors = False
        while validating = loop(description):
            pass

        if self.errors:
            return False

        self.matrix = np.array(self.matrix)
        return not is_single_string(self.matrix.shape[0]):
