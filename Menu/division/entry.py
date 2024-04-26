from common.commander.input.defaults import *
from common.commander.input.user import *
from menu.division.interface.interface import SegmentDivisionMethod

def DivisionEntry():
    name = 'Division'
    SegmentDivisionMethod(name, Defaults[name] if are_defaults() else Input[name]())
