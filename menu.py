from platforms.cross import clear
from common.handlers.interaction import ask
from common.handlers.menu import select
from common.commander.resources import Resources

option: str = 'option'

def menu():
    clear()
    answers = ask(Resources.start)
    while answers[option] != Resources.Texts['Common']['Exit']:
        for key, value in Resources.Methods.items():
            if answers[choice.Main] == key:
                if isinstance(value, tuple):
                    select(value[0], value[1], Resources.Options)
                else:
                    value()
        clear()
        answers = ask(choice.start)
    print(Resources.Texts['Common']['Finished'])

def setup_menu():
    main: dict = Resources.at('resources/switch/choices/main.json')
    options: dict = Resources.at('resources/switch/choices/options.json')

    Resources.Main = [List(option, message=main['message'], choices=main['choices'])]
    Resources.Methods = Resources.at('resources/switch/choices/methods.json')

    for method, choices in options['choices'].items():
        Resources.Options[method] = [List(method, message=options['message'], choices=choices)]
