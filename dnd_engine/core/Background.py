_registeredBackgrounds = {}

def registered(cls):
    _registeredBackgrounds[cls.__name__] = cls
    return cls


def sourcebook(bookName):
    def decorator(cls):
        setattr(cls, '_sourcebook', bookName)
        return cls
    return decorator


def getAvailableBackgrounds():
    return _registeredBackgrounds


class Background:
    def __init__(self, name, skillProf=None, toolProf=None, languages=None, equipment=None, features=None):
        self.name = name
        self.skillProf = skillProf if skillProf else []
        self.toolProf = toolProf if toolProf else []
        self.languages = languages if languages else []
        self.equipment = equipment if equipment else []
        self.features = features if features else []
        