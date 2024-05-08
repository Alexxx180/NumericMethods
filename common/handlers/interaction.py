from inquirer import prompt
from platforms.cross import clear
from common.commander.resources import Resources

line = { 'up': '\033[3A' }

def truncate(count: int):
    for i in range(0, count + 1):
        print(' ', end='')
    print()

def pause(text: str = ""):
    message = Resources.Texts['Common']['Forward']
    print(text, message) ; input()
    print(line['up']) ; truncate(len(message))

def ask(query: list) -> dict:
    answers = prompt(query) ; clear()
    return answers
