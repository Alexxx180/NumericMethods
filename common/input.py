import common.input.common

# Выбор Да-Нет
def UserSelect(query):
    accept, decline = UserQuery(query)

    while not (accept or decline):
        accept, decline = UserQuery(query)

    return accept
