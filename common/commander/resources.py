from json import load

class Resources:
    @staticmethod
    def at(path: str) -> dict:
        with open(path) as data:
            return load(data)

    # Tables / Plots switch
    Enabled: dict
    Hints: dict

    # Table fields / text labels
    Fields: dict
    Texts: dict

    # User input / defaults
    Defaults: dict 
    Input: dict
    Queries: dict

    # Menu choices
    Main: dict
    Methods: dict
    Options: dict
