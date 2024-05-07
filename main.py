from start import dropdown, setup_menu
from common.handlers.input.specific import setup_input
from common.commander.resources import Resources

variant: int

def resource(file):
    if isinstance(file, dict):
        resources: dict = {}
        for key, value in file.items():
            resources[key] = resource(value)
        return resources
    elif isinstance(file, list):
        no: int = variant % file[1] + 1
        return Resources.at(f'resources/{file[0]}/{no}.json')
    else:
        return Resources.at(f'resources/{file}.json')


def main():
    manifest: dict = Resources.at('resources/manifest.json')

    for name in ('Texts', 'Fields', 'Hints', 'Enabled', 'Defaults', 'Formula'):
        setattr(Resources, name, resource(manifest[name]))

if __name__ == '__main__':
    with open('variant.txt') as no:
        variant = int(no.readline())
    main()
    setup_input(Resources.at('resources/texts/queries.json'))
    setup_menu()
    dropdown()
