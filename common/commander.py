from common.input import UserSelect

class Commander:
    @staticmethod
    def View(control: str, method: str):
        return Enabled[control][method] or UserSelect(Texts[control][method])

    Enabled = {
        'Tables': {
            'Simpson' : True
        },
        'Plots': {
            'Simpson' : True,
            'Tangent' : False
        }
    }

    Texts = {
        'Tables': {
            'Simpson' : 'Показать таблицу расчетов? (y/n)'
        }
        'Plots': {
            'Simpson' : 'Показать график? (y/n)',
            'Tangent' : 'Показать график касательной? (y/n)'
        }
    }

