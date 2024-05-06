#from menu import menu
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
        #return f'resources/{file[0]}/{no}.json'
        return Resources.at(f'resources/{file[0]}/{no}.json')
    else:
        #return f'resources/{file}.json'
        return Resources.at(f'resources/{file}.json')


def main():
    manifest: dict = Resources.at('resources/manifest.json')

    Resources.Texts = resource(manifest['Texts'])
    Resources.Fields = resource(manifest['Fields'])
    Resources.Hints = resource(manifest['Hints'])
    Resources.Enabled = resource(manifest['Enabled'])
    Resources.Defaults = resource(manifest['Defaults'])
    Resources.Formula = resource(manifest['Formula'])

    print(Resources.Formula)

if __name__ == '__main__':
    with open('variant.txt') as no:
        variant = int(no.readline())
    main()
    #setup_queries(Resources.at('resources/texts/queries.json'))
    #setup_menu()
    #menu()
