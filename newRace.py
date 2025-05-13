_registeredRaces = {}


def registered(cls):
    _registeredRaces[cls.__name__] = cls
    return cls


def sourcebook(bookName):
    def decorator(cls):
        setattr(cls, '_sourcebook', bookName)
        return cls
    return decorator


def getAvailableRaces():
    return _registeredRaces


class Race:
    def __init__(self, name, creatureType, abilityBonuses, racialTraits, toolProf, languages, size, speed, flySpeed=0, swimSpeed=0, climbSpeed=0, burrowSpeed=0):
        self.name = name
        self.creatureType = creatureType
        self.abilityBonuses = abilityBonuses
        self.racialTraits = racialTraits
        self.toolProf = toolProf
        self.languages = languages
        self.size = size
        self.speed = speed
        self.flySpeed = flySpeed
        self.swimSpeed = swimSpeed
        self.climbSpeed = climbSpeed
        self.burrowSpeed = burrowSpeed
            

########### PROTOS ##############


#@registered
@sourcebook("")
class NEW_RACE_NAME(Race):
    def __init__(self):
        super().__init__(
            name="",
            creatureType="Humanoid",
            abilityBonuses={
                "": 0,
                "": 0
            },
            racialTraits=[
                "",
                "",
                ""
            ],
            toolProf=[],
            languages=[
                "Common",
                ""
            ],
            size="Medium",
            speed=25,
            flySpeed=0,
            swimSpeed=0,
            climbSpeed=0,
            burrowSpeed=0
        )


#@registered
@sourcebook("")
class NEW_RACE_NAME_SUBRACE(NEW_RACE_NAME):
    def __init__(self):
        super().__init__()
        self.name = ""
        self.abilityBonuses.update({})
        self.racialTraits.extend([])
        # Modify other attributes if needed
        
        