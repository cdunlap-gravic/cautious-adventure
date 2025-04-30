class Character:
    def __init__(self, name, race, background, alignment, base_attributes):
        """
        Initializes a new character.

        Args:
            name (str): The character's name.
            race (str): The character's race.
            background (str): The character's background.
            alignment (str): The character's alignment.
            base_attributes (dict): A dictionary containing the character's  base ability scores (e.g. {"strength":15, "dexterity": 12, ...}). 
        """
        self.name = name
        self.race = race
        self.background = background
        self.alignment = alignment
        self.base_attributes = base_attributes
        self.level_bonuses = {attr: 0 for attr in base_attributes} # Bonuses from level-based ASIs
        self.equipment_bonuses = {attr: 0 for attr in base_attributes}
        self.boon_bonuses = {attr: 0 for attr in base_attributes}
        self.curse_penalties = {attr: 0 for attr in base_attributes}
        self.hit_points = {"current": 0, "maximum": 0, "temporary": 0}
        self.armor_class = 0
        self.initiative_bonus = 0
        self.speed = 0
        self.classes = {} # Dictionary to store class levels: {"Fighter": 3, "Wizard" : 2}
        self.level_history = [] # List of (class_name, level_gained) tuples
        self.proficiency_bonus = 2 # Base proficiency bonus starts at +2
        
    def get_attribute_score(self, attribute):
        """
        Calculates the current effective score fore a given attribute.
        """
        base = self.base_attributes.get(attribute, 0)
        level_bonus = self.level_bonuses.get(attribute, 0)
        equipment_bonus = self.equipment_bonuses.get(attribute, 0)
        boon_bonus = self.boon_bonuses.get(attribute, 0)
        curse_penalty = self.curse_penalties.get(attribute, 0)        
        return base + level_bonus + equipment_bonus + boon_bonus - curse_penalty
        
    def get_attribute_modifier(self, attribute):
        """
        Calculates the modifier for a given attribute score.
        """
        score = self.get_attribute_score(attribute)
        return (score // 2) - 5 # Floor division to round down
        
    def add_level(self, class_name):
        """
        Increases the level in a specific class.
        """
        self.classes[class_name] = self.classes.get(class_name, 0) + 1
        self.level_history.append((class_name, self.classes[class_name]))
        self._update_proficiency_bonus() # Recalculate proficiency bonus on level up
        #TODO trigger other level-based stat increases and otehr class feature unlocks etc.
        
    def reduce_level(self, class_name, levels_to_reduce=1, revert_stats=False):
        """
        Reduces the level in a specific class. Can optionally revert level_based stat increases. Possibly useful for rollback of levels, or a curse.
        """
        if class_name in self.classes and self.classes[class_name] > 0:
            self.classes[class_name] -= levels_to_reduce
            if self.classes[class_name] < 0:
                self.classes[class_name] = 0 # Ensure level doesn't go below 0
            
            #TODO implement log ic to handle level history and potentially revert stats based on the 'revert_stats' flag and the level history. This will be more complex.
            print(f"{self.name}'s level in {class_name} reduced to {self.classes[class_name]}.")
            self._update_proficiency_bonus() # Recalculate proficiency bonus on level down
    
    def _update_proficiency_bonus(self):
        """
        Calculates the profieciency bonus basedo nthe character's total level.
        """
        total_level = sum(self.classes.values())
        if total_level < 5:
            self.proficiency_bonus = 2
        elif total_level < 9:
            self.proficiency_bonus = 3
        elif total_level < 13:
            self.proficiency_bonus = 4
        elif total_level < 17:
            self.proficiency_bonus = 5
        else:
            self.proficiency_bonus = 6
    
    def apply_equipment_bonus(self, attribute, bonus):
        """
        Applies a bonus to an attribute from equipment.
        """
        self.equipment_bonuses[attribute] = self.equipment_bonuses.get(attribute, 0) + bonus
    
    def remove_equipment_bonus(self, attribute, bonus):
        """
        Removes a bonus to an attribute from equipment.
        """
        self.equipment_bonuses[attribute] = max(0, self.equipment_bonuses.get(attribute, 0) - bonus)
    
    #TODO add simlar methods for boon bonuses and curse penalties
    
#example instantiation:
if __name__ == "__main__":
    my_character = Character(
        name="Anya",
        race="Half-Elf",
        background="Noble",
        alignment="Chaotic Good",
        base_attributes={
            "STR": 14,
            "DEX": 13,
            "CON": 15,
            "INT": 10,
            "WIS": 12,
            "CHA": 8
        }
    )
    
    print(f"{my_character.name}'s Strength: {my_character.get_attribute_score('STR')}")
    print(f"{my_character.name}'s Strength Modifier: {my_character.get_attribute_modifier('STR')}")

    my_character.add_level("Fighter")
    my_character.add_level("Fighter")
    my_character.add_level("Wizard")
    print(f"{my_character.name}'s Levels: {my_character.classes}")
    print(f"{my_character.name}'s Proficiency Bonus: +{my_character.proficiency_bonus}")

    my_character.apply_equipment_bonus("STR", 2)
    print(f"{my_character.name}'s Strength with Equipment Bonus: {my_character.get_attribute_score('STR')}")