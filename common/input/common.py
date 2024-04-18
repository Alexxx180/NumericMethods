import inquirer

# Клавиши выбора
yes = { 'y', 'Y', 'н', 'Н' }
no = { 'n', 'N', 'т', 'Т' }

# Проверка ввода да-нет
def UserQuery(query):
    print(query)
    user = input()
    accept = user in yes
    decline = user in no
    return accept, decline

# Ввод переменных
def vinput(query):
    return inquirer.prompt(query)
