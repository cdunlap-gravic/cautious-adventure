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
    def __init__(self, name, hitDie, savingThrowProf, skillProf, weaponProf, toolProf, armorProf, startingEquipment, levelFeatures, spellSlotTree=None, cantripsKnownAtLevel=None, spellsKnownAtLevel=None):
        self.name = name
        self.hitDie = hitDie
        self.savingThrowProf = savingThrowProf
        self.skillProf = skillProf
        self.weaponProf = weaponProf if weaponProf else []
        self.toolProf = toolProf if toolProf else []
        self.armorProf = armorProf if armorProf else []
        self.startingEquipment = startingEquipment if startingEquipment else []
        self.levelFeatures = levelFeatures if levelFeatures else {}
        self.spellSlotTree = spellSlotTree if spellSlotTree else None
        self.cantripsKnownAtLevel = cantripsKnownAtLevel if cantripsKnownAtLevel else {}
        self.spellsKnownAtLevel = spellsKnownAtLevel if spellsKnownAtLevel else {}
        self.spellPool = None #TODO Need to implement this... Later. I do NOT want to write out the entire spellpool in 5e right now...
        

        
    #@ EVENTUALLY I SHOULD BE TURNING THESE STRINGS INTO DIRECT CALLS TO OBJECTS
    
    

#@registered
#@sourcebook("PHB'14")
class _(Class):
    def __init__(self):
        super().__init__(
            name="",
            hitDie=12,
            savingThrowProf=[
                "",
                ""
            ],
            skillProf={
                2: [
                    "",
                    "",
                ]
            },
            weaponProf=[
                "",
                ""
            ],
            toolProf=[],
            armorProf=[
                "",
                "",
                ""
            ],
            startingEquipment=None,
            levelFeatures={
                1: [""],
                2: [""],
                3: [""],
                4: [""],
                5: [""],
                6: [""],
                7: [""],
                8: [""],
                9: [""],
                10: [""],
                11: [""],
                12: [""],
                13: [""],
                14: [""],
                15: [""],
                16: [""],
                17: [""],
                18: [""],
                19: [""],
                20: [""]
            }
        )