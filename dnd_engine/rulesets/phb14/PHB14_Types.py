from enum import Enum

class PHB14_Languages(Enum):
    ABYSSAL = ("Abyssal", "Exotic", "Infernal") # Abyssal uses the Infernal script
    CELESTIAL = ("Celestial", "Exotic", "Celestial")
    COMMON = ("Common", "Standard", "Common")
    DEEP_SPEECH = ("Deep Speech", "Exotic", "None") # Deep Speech has no written form
    DRACONIC = ("Draconic", "Exotic", "Draconic")
    DRUIDIC = ("Druidic", "Secret", "None")
    DWARVISH = ("Dwarvish", "Standard", "Dwarvish")
    ELVISH = ("Elvish", "Standard", "Elvish")
    GIANT = ("Giant", "Standard", "Dwarvish") # Giant uses the Dwarvish script
    GNOMISH = ("Gnomish", "Standard", "Dwarvish") # Gnomish uses the Dwarvish script
    GOBLIN = ("Goblin", "Standard", "Dwarvish") # Goblin uses the Dwarvish script
    HALFLING = ("Halfling", "Standard", "Common") # Halfling uses the Common script
    INFERNAL = ("Infernal", "Exotic", "Infernal")
    ORC = ("Orc", "Standard", "Dwarvish") # Orc uses the Dwarvish script
    PRIMORDIAL = ("Primordial", "Exotic", "Dwarvish")
    SYLVAN = ("Sylvan", "Exotic", "Elvish")
    THIEVES_CANT = ("Thieves' Cant", "Secret", "None")
    UNDERCOMMON = ("Undercommon", "Exotic", "Elvish")

    def __init__(self, value, type, script):
        self._value_ = value
        self.type = type
        self.script = script

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name} {self.value}"