from inquirer import prompt
from platforms.cross import clear

def pause(text: str = ""):
    print(text, "Нажмите Enter для продолжения...") # Перед остановкой консоли
    input()  # Останавливаем консоль и ждем ввода от пользователя

def ask(query: tuple) -> dict:
    answers = prompt(query)
    clear()
    return answers

def select(invoke: callable, query: str, choices: dict):
    answers = ask(query)
    for key, value in choices:
        if answers[query] == key:
            invoke(value)
