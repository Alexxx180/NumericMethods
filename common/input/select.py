from functools import reduce
import operator

keys = {
    'yes': ('y', 'Y', 'н', 'Н'),
    'no': ('n', 'N', 'т', 'Т')
}

def __user_query(query):
    user = pause(query, "")
    accept = user in keys['yes']
    decline = user in keys['no']
    return (accept, decline)

def user_select(query) -> bool:
    accept = __user_query(query)

    while not reduce(operator.or, accept):
        accept = user_query(query)

    return accept[0]
