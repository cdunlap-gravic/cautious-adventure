from enum import Enum
from dataclasses import dataclass, field
from typing import List
class AbilityScore(Enum):
    """
    Represents the six core ability scores in D&D 5th Edition,
    with an associated description.
    """
    # Each member has two arguments: the shortName (value) and the description
    STRENGTH = ("STR", "Measures physical power, training, and the extent to which you can exert raw physical force.")
    DEXTERITY = ("DEX", "Measures agility, reflexes, and balance.")
    CONSTITUTION = ("CON", "Measures health, stamina, and vital force.")
    INTELLIGENCE = ("INT", "Measures mental acuity, accuracy of recall, and the ability to reason.")
    WISDOM = ("WIS", "Measures how attuned you are to the world around you and represents perceptiveness and intuition.")
    CHARISMA = ("CHA", "Measures your ability to interact effectively with others through confidence, eloquence, or a commanding presence.")
    FLEX = ("FLEX", "Please choose an ability score to increase by 1.")
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"AbilityScore.{self.name} ('{self.value}')"

    def fullDescription(self):
        return f"{self.name} ({self.value}): {self.description}"



class Size(Enum):
    TINY = ("Tiny", 2.5)
    SMALL = ("Small", 5)
    MEDIUM = ("Medium", 5)
    LARGE = ("Large", 10)
    HUGE = ("Huge", 15)
    GARGANTUAN = ("Gargantuan", 20)
    # SPECIAL = ("<Special>", 20) #fill in the blank size. defaults to 20, but can be larger.
    
    def __init__(self, name, space):
        self._value_ = name
        self.space = space
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Size.{self.name}, takes {self.space}' x {self.space}' area of the board"
    

class Skill(Enum):
    """
    Represents the 18 core skills in D&D 5th Edition.
    Each skill has a name and a governing ability score.
    """
    ACROBATICS = ("Acrobatics", AbilityScore.DEXTERITY)
    ANIMAL_HANDLING = ("Animal Handling", AbilityScore.WISDOM)
    ARCANA = ("Arcana", AbilityScore.INTELLIGENCE)
    ATHLETICS = ("Athletics", AbilityScore.STRENGTH)
    DECEPTION = ("Deception",AbilityScore.CHARISMA)
    HISTORY = ("History", AbilityScore.WISDOM)
    INSIGHT = ("Insight", AbilityScore.WISDOM)
    INTIMIDATION = ("Intimidation", AbilityScore.CHARISMA)
    INVESTIGATION = ("Investigation", AbilityScore.INTELLIGENCE)
    MEDICINE = ("Medicine", AbilityScore.WISDOM)
    NATURE = ("Nature", AbilityScore.INTELLIGENCE)
    PERCEPTION = ("Perception", AbilityScore.WISDOM)
    PERFORMANCE = ("Performance", AbilityScore.CHARISMA)
    PERSUASION = ("Persuasion", AbilityScore.CHARISMA)
    RELIGION = ("Religion", AbilityScore.INTELLIGENCE)
    SLEIGHT_OF_HAND = ("Sleight of Hand", AbilityScore.DEXTERITY)
    STEALTH = ("Stealth", AbilityScore.DEXTERITY)
    SURVIVAL = ("Survival", AbilityScore.WISDOM)
    
    def __init__(self, name: str, abilityScore: AbilityScore):
        self._value_ = name # The primary string value for the enum member
        self.abilityScore = abilityScore

    def __str__(self):
        return self.value   # Returns "Acrobatics", "Athletics", etc.

    def __repr__(self):
        return f"Skill.{self.name} ('{self.value}', related to {self.abilityScore})"

    @property
    def relatedAbilityShort(self) -> str:
        return self.abilityScore.value


@dataclass(frozen=True)
class FlexConfig:
    count: int = 1
    value: int = 1
    exclude: List[AbilityScore] = field(default_factory=list)