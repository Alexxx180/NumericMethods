from common.commander.formula.text import *
from common.commander.defaults import *
from common.commander.input import *
from menu.division.interface import DivisionMethod

def DivisionEntry():
    DivideSegmentMethod(Defaults['Division'] if are_defaults() else Input['Division']())
