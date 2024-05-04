from platforms.cross import clear
from common.handlers.interaction import ask, select
import common.commander.input.choices as choice

# TODO: For each formula except Gauss
# TODO: For sympson append formula separately before any method execution
def menu():
    clear()
    answers = ask(choice.start)
    while answers[choice.Main] != 'Выход':
        for key, value in choice.methods.items():
            if answers[choice.Main] == key:
                if isinstance(value, tuple):
                    select(value[0], value[1], value[2], choice.options)
                else:
                    value()
        clear()
        answers = ask(choice.start)
    print("Завершение работы.")
