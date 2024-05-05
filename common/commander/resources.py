from json import load

class Resources:
    @staticmethod
    def at(path: str) -> dict:
        with open(path) as data:
            return load(data)

    # Tables / Plots switch
    Enabled: dict
    Queries: dict

    Fields: dict # All table fields
    Texts: dict # All text labels

    Defaults: dict # All input defaults

    # Menu choices
    Main: dict
    Methods: dict
    Options: dict
