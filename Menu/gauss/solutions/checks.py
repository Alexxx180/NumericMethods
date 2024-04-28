import numpy as np
from common.commander.texts.common import *

def are_undefined(array, text):
    for row in array:
        if np.all(row[:-1] == 0) and row[-1] != 0:
            return text.empty(row, 'None')
        if np.all(row == 0):
            return text.empty(row, 'Many')

    index: int = array.shape[0] - 1
    row = array[index]

    if all(e == 0 for e in row[:-2]):
        return text.zeros()

    return False

def is_suitable(shape):
    return shape[0] <= shape[1] - 1

def is_varying(self, text):
    values: list = self.values
    matrix: list = self.matrix
    
    if errors := len(set(map(len, matrix + [values]))) > 1:
        text.varying()
    return errors

def is_single(count: int, text):
    if errors := count == 1:
        text.single()
    return errors
