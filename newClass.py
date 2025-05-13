_registeredClasses = {}


def registered(cls):
    _registeredClasses[cls.__name__] = cls
    return cls


def sourcebook(bookName):
    def decorator(cls):
        setattr(cls, '_sourcebook', bookName)
        return cls
    return decorator


def getAvailableClasses():
    return _registeredClasses


class newClass:
    def __init__(self, name, hitDice, savingThrowProf):
        pass


class Class:
    def __init__(self, name, hitDice, savingThrowProf, skillProf, levelFeatures):
        self.name = name
        self.hitDice = hitDice
        self.savingThrowProf = savingThrowProf
        self.skillProf = skillProf
        self.levelFeatures = levelFeatures

####?! WHY DO I NEED THESE FUNCTIONS? THESE SHOULD BE CALCULATED HERE? THIS SHOULD COME FROM CHARACTER. Character should be calculating any stats, not the class. Class should only handle things related to the class itself.
 
    def getSkillProfAtLevel(self, level):
        if level in self.skillProf:
            if isinstance(self.skillProf[level], tuple):
                return self.skillProf[level]
            else:
                # For level 2+ skill proficiencies (just a list), no choices are given
                return (0, self.skillProf[level])
        return (0, [])

    def getSavingThrowProf(self):
        return self.savingThrowProf
    
    def getLevelFeatures(self, level):
        return self.levelFeatures.get(level, [])
