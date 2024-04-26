from common.commander.texts.common import *

class Printer:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add(self, text: callable, key: str, *args):
        self.orders.append((text, key, args))
        return self

    def print(self):
        for order in self.orders:
            text: callable = order[0]
            key: str = order[1]
            args: int = 2

            if len(order) > args:
                text(Texts[self.name][key].format(*order[args]))
            else:
                text(Texts[self.name][key])
        return self

    def clear(self):
        self.orders.clear()
        return self
