from inquirer import prompt
from platforms.cross import clear

def upline():
    print('\033[3A')

def truncate(count: int):
    for i in range(0, count):
        print(' ', end='')
    print()

def pause(text: str = ""):
    print(text)
    message = "Нажмите Enter для продолжения..."
    print(message)
    input()
    upline()
    truncate(len(message))

def ask(query: list) -> dict:
    answers = prompt(query)
    clear()
    return answers

def select(invoke: callable, query: str, choices: dict, options: dict):
    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke(value)
