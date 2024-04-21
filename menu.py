from platforms.cross import clear
from common.handlers.interaction import ask, select
import common.commander.input.choices as choice

# TODO: For each formula except Gauss
# TODO: For sympson append formula separately before any method execution
def menu():
    clear()
    answers = ask(choice.start)
    while answers[choice.Main] != 'Выход':
        for key, value in choice.methods:
            if answers[choice.Main] == key:
                invoke = value[0]
                if len(value) == 1:
                    invoke()
                else:
                    select(invoke, values[1], values[2])
        clear()
        answers = ask(start_menu)
    print("Завершение работы.")


if __name__ == '__main__':
    menu()
