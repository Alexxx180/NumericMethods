from inquirer import prompt, Confirm

def View(control: str, method: str):
    message = Texts[control][method]
    confirm = [Confirm('c', message=message, default=True)]
    return Enabled[control][method] or prompt(confirm)['c']

Enabled = {
    'Tables': {
        'Simpson' : True
    },
    'Plots': {
        'Division': True,
        'Simpson' : True,
        'Tangent' : False
    }
}

Texts = {
    'Tables': {
        'Simpson' : 'Показать таблицу расчетов?'
    },
    'Plots': {
        'Division' : 'Показать график?',
        'Simpson' : 'Показать график?',
        'Tangent' : 'Показать график касательной?'
    }
}

