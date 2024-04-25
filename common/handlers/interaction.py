from inquirer import prompt
from platforms.cross import clear

def pause(text: str = ""):
    print(text, "Нажмите Enter для продолжения...")
    input()

def ask(query: list) -> dict:
    answers = prompt(query)
    clear()
    return answers

def select(invoke: callable, query: str, choices: dict, options: dict):
    answers = ask(options[query])
    for key, value in choices.items():
        if answers[query] == key:
            invoke(value)
