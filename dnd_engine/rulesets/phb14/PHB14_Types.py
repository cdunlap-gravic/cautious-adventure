from enum import Enum

class PHB14_Languages(Enum):
    # Enum member name = (Language Name, Written Script)
    COMMON = ("Common", "Common")
    INFERNAL = ("Infernal", "Infernal")
    ELVISH = ("Elvish", "Elvish")
    DWARVISH = ("Dwarvish", "Dwarvish")
    GIANT = ("Giant", "Dwarvish") # Giant uses the Dwarvish script
    GOBLIN = ("Goblin", "Dwarvish") # Goblin uses the Dwarvish script
    ORC = ("Orc", "Dwarvish") # Orc uses the Dwarvish script
    DRACONIC = ("Draconic", "Draconic")
    HALFLING = ("Halfling", "Common") # Halfling uses the Common script
    GNOMISH = ("Gnomish", "Dwarvish") # Gnomish uses the Dwarvish script
    ABYSSAL = ("Abyssal", "Infernal") # Abyssal uses the Infernal script
    CELESTIAL = ("Celestial", "Celestial")
    DEEP_SPEECH = ("Deep Speech", "None") # Deep Speech has no written form
    PRIMORDIAL = ("Primordial", "Dwarvish")
    SYLVAN = ("Sylvan", "Elvish")
    UNDERCOMMON = ("Undercommon", "Elvish")
    # ... add all other PHB14 languages with their script

    @property
    def name(self):
        """Returns the full name of the language (e.g., 'Common')."""
        return self.value[0]

    @property
    def script(self):
        """Returns the name of the script used (e.g., 'Common', 'Elvish')."""
        return self.value[1]

    def __str__(self):
        """Allows printing the enum member to get its primary name."""
        return self.name

    def __repr__(self):
        """For debugging, shows both enum name and its tuple value."""
        return f"{self.__class__.__name__}.{self.name} {self.value}"