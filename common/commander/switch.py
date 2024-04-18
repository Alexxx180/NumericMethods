from common.input.select import user_select

class Switch:
    @staticmethod
    def View(control: str, method: str):
        return Enabled[control][method] or user_select(Texts[control][method])

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

