from enum import Enum
from AbilityScore import AbilityScore

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
        # Customize representation for debugging/display
        return f"Skill.{self.name} ('{self.value}', related to {self.abilityScore})"

    @property
    def relatedAbilityShort(self) -> str:
        return self.abilityScore.value
