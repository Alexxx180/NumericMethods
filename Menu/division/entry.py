from Division_segment.main import Division_segment 
from Classes.Input import vinput, validate_e
from Menu.common import request_a_b, request_n
import Classes.Texts.Queries as q

def DivisionEntry():
    args = Defaults['Division'] if are_defaults else Input['Division']()
    DivisionMethod(args)
