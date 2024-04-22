import numpy as np
from common.commander.texts.common import *

def __null_string(name: str, row: list):
    text = Texts['Gauss']['Solutions']
    return (True, text['Common'].format(row) + text[name])

def __all_zeros(array: list):
    text = Texts['Gauss']['Solutions']['Endless']
    return (all(e == 0 for e in array[:-2]), text)

def are_undefined(array):
    for row in array:
        if np.all(row[:-1] == 0) and row[-1] != 0:
            return __null_string(row, 'None')
        if np.all(row == 0):
            return __null_string(row, 'Many')

    index: int = array.shape[0] - 1

    return __all_zeros(array[index])

def is_suitable(shape):
    return shape[0] <= shape[1] - 1

def is_varying(self):
    values: list = self.values
    matrix: list = self.matrix
    
    if errors := len(set(map(len, matrix + [values]))) > 1:
        pause(Texts['Gauss']['Input']['Count'])
    return errors

def is_single_string(count: int):
    if errors := count == 1:
        pause(Texts['Gauss']['Input']['Single'])
    return errors
