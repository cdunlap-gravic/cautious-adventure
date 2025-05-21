from enum import Enum

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

    def __init__(self, shortName, description):
        # The first argument passed to the Enum member becomes its .value
        self._value_ = shortName
        self.description = description

    def __str__(self):
        # Customize string representation to show the short name
        return self.value

    def __repr__(self):
        # Customize representation for debugging/display
        return f"AbilityScore.{self.name} ('{self.value}')"

    def fullDescription(self):
        return f"{self.name} ({self.value}): {self.description}"

# --- How to access the description field ---

print(AbilityScore.STRENGTH.value)         # Output: STR
print(AbilityScore.STRENGTH.name)          # Output: STRENGTH
print(AbilityScore.STRENGTH.description)   # Output: Measures physical power, training...

print("\n--- All Ability Scores with Descriptions ---")
for score in AbilityScore:
    print(score.fullDescription())

# savingThrowProf=[AbilityScore.STRENGTH, AbilityScore.CONSTITUTION]
# spellcastingAbility=AbilityScore.INTELLIGENCE