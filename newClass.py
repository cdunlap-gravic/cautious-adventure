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


class Class:
    def __init__(self, name, hitDie, savingThrowProf, skillProf, weaponProf, armorProf, startingEquipment, levelFeatures, spellSlotTree=None, spellsKnownAtLevel=None, cantripsKnownAtLevel=None):
        self.name = name
        self.hitDie = hitDie
        self.savingThrowProf = savingThrowProf
        self.skillProf = skillProf
        self.weaponProf = weaponProf if weaponProf else []
        self.armorProf = armorProf if armorProf else []
        self.startingEquipment = startingEquipment if startingEquipment else []
        self.levelFeatures = levelFeatures if levelFeatures else {}
        self.spellSlotTree = spellSlotTree if spellSlotTree else None
        self.spellsKnownAtLevel = spellsKnownAtLevel if spellsKnownAtLevel else {}
        self.cantripsKnownAtLevel = cantripsKnownAtLevel if cantripsKnownAtLevel else {}
        self.spellPool = None
        

        
    #@ EVENTUALLY I SHOULD BE TURNING THESE STRINGS INTO DIRECT CALLS TO OBJECTS
    

# Just gotta populate the rest of the classes and we're good to push a commit! Screw it, I at least got the structure finalized, that's worth a commit