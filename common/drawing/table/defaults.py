from prettytable import PrettyTable

def TableDefaults(title: str) -> PrettyTable:
    align = { 'Left': 'l', 'Center': 'c', 'Right': 'r' }

    table = PrettyTable()
    table.align = align['Right']
    table.title = title
    table.float_format = '.8'

    return table
