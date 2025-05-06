_registeredRaces = {}

def registeredRace(cls):
    _registeredRaces[cls.__name__] = cls
    return cls

class Race:
    def __init__(self, name, abilityBonuses, racialTraits, speed, languages, size):
        self.name = name
        self.abilityBonuses = abilityBonuses
        self.racialTraits = racialTraits
        self.speed = speed
        self.languages = languages
        self.size = size

@registeredRace
class Human(Race):
    def __init__(self):
        super().__init__(
            name="Human",
            abilityBonuses={
                "STR": 1, 
                "DEX": 1, 
                "CON": 1, 
                "INT": 1, 
                "WIS": 1, 
                "CHA": 1
            },
            racialTraits=["Extra Language"], # We'll handle the choice later
            speed=30,
            languages=["Common"],
            size="Medium"
        )

@registeredRace
class Dwarf(Race):
    def __init__(self):
        super().__init__(
            name="Dwarf",
            abilityBonuses={"CON": 2},
            racialTraits=[
                "Darkvision", 
                "Dwarven Resilience", 
                "Dwarven Combat Training"
            ],
            speed=25,
            languages=[
                "Common", 
                "Dwarvish"
            ],
            size="Medium"
        )

def getAvailableRaces():
    return _registeredRaces