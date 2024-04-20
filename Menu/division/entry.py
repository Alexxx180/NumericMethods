from common.commander.defaults import *
from common.commander.input import *
from menu.division.interface import DivisionSegmentMethod

def DivisionEntry():
    name = 'Division'
    DivideSegmentMethod(Defaults[name] if are_defaults() else Input[name]())
