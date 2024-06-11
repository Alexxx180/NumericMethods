import matplotlib
from common.handlers.interaction import pause
from common.handlers.input.specific import setup_input
from common.commander.resources import Resources
from start import dropdown, setup_menu

variant: int

def resource(file):
    if isinstance(file, dict):
        resources: dict = {}
        for key, value in file.items():
            resources[key] = resource(value)
        return resources
    elif isinstance(file, list):
        start: int = 1
        no: int = (variant - start) % file[1] + start
        print(Resources.Texts["Common"]["Variant"].format(file[0], file[1], no))

        return Resources.at(f'resources/{file[0]}/{no}.json')
    else:
        return Resources.at(f'resources/{file}.json')


def main():
    manifest: dict = Resources.at('resources/manifest.json')

    for name in ('Texts', 'Fields', 'Hints', 'Enabled', 'Defaults', 'Formula'):
        setattr(Resources, name, resource(manifest[name]))

if __name__ == '__main__':
    matplotlib.use('TkAgg')

    with open('variant.txt') as no:
        variant = int(no.readline())

    print("Program No {0}, Variants check...\n".format(variant))
    main()
    setup_input(Resources.at('resources/texts/queries.json'))
    setup_menu()
    pause()
    dropdown()
