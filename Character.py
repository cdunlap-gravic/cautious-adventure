import json

from Class import getAvailableClasses
from Background import getAvailableBackgrounds
from Race import getAvailableRaces
from SaveSystem import save_character, load_character

AVAILABLE_CLASSES = getAvailableClasses()
AVAILABLE_BACKGROUNDS = getAvailableBackgrounds()
AVAILABLE_RACES = getAvailableRaces()

def logMessage(level, message):
    #placeholder for our logging system
    print(f"[{level.upper()}] {message}")
    

class Character:
    def __init__(self, name, race, background, alignment, baseAttributes, feats=None):
        """
        Initializes a new character.

        Args:
            name (str): The character's name.
            race (str): The character's race.
            background (str): The character's background.
            alignment (str): The character's alignment.
            baseAttributes (dict): A dictionary containing the character's  base ability scores (e.g. {"strength":15, "dexterity": 12, ...}).
        
        Params: #TODO flesh this list out later
            name
            race -> should point to a chart to pull stats/traits from
            background
            alignment
            base attributes
                STR, 
            ...
        """
        self.name = name
        self.race = race
        self.background = background
        self.alignment = alignment
        self.baseAttributes = baseAttributes
        self.levelBonuses = {attr: 0 for attr in baseAttributes} # Bonuses from level-based ASIs
        self.equipmentBonuses = {attr: [] for attr in baseAttributes}
        self.boonBonuses = {attr: [] for attr in baseAttributes}
        self.cursePenalties = {attr: [] for attr in baseAttributes}
        self.attributeOverrides = {} # {attribute: (source, override_value)} This is for hard overrides like INT = 19.
        self.hitPoints = {"current": 0, "maximum": 0, "temporary": 0}
        self.armorClass = 0
        self.initiativeBonus = 0
        
        #@ Movement Speeds 
        self.speed = 0
        self.flySpeed = 0
        self.swimSpeed = 0
        self.climbSpeed = 0
        self.burrowSpeed = 0
        
        self.classes = {} # Dictionary to store class levels: {"Fighter": 3, "Wizard" : 2}
        self.levelHistory = [] # List of (className, level_gained) tuples
        self.profBonus = 2 # Base proficiency bonus starts at +2
        self.feats = feats if feats is not None else []
        self.skills = {
            "Athletics": False,
            "Acrobatics": False,
            "Sleight of Hand": False,
            "Stealth": False,
            "Arcana": False,
            "History": False,
            "Investigation": False,
            "Nature": False,
            "Religion": False,
            "Animal Handling": False,
            "Insight": False,
            "Medicine": False,
            "Perception": False,
            "Survival": False,
            "Deception": False,
            "Intimidation": False,
            "Performance": False,
            "Persuasion": False
        }
        self.savingThrowProf = {
            "STR": False,
            "DEX": False,
            "CON": False,
            "INT": False,
            "WIS": False,
            "CHA": False
        }
        self.racialTraits = []
        self.languages = []
        self.size = "Medium" # Default size
        
        # Apply background skill prociciencies
        if self.background and self.background in AVAILABLE_BACKGROUNDS:
            background_obj = AVAILABLE_BACKGROUNDS[self.background]()
            for skill in background_obj.skillProf:
                self.applySkillProf(skill)
        
        # Apply racial traits
        if self.race and self.race in AVAILABLE_RACES:
            race_obj = AVAILABLE_RACES[self.race]()
            self.speed = race_obj.speed
            self.flySpeed = race_obj.flySpeed
            self.swimSpeed = race_obj.swimSpeed
            self.climbSpeed = race_obj.climbSpeed
            self.burrowSpeed = race_obj.burrowSpeed
            self.languages.extend(race_obj.languages)
            self.size = race_obj.size
            self.racialTraits.extend(race_obj.racialTraits)
            for ability, bonus in race_obj.abilityBonuses.items():
                if ability in self.baseAttributes:
                    self.baseAttributes[ability] += bonus
        
    def getAttributeScore(self, attribute):
        """
        Calculates the current effective score fore a given attribute.
        """
        base = self.baseAttributes.get(attribute, 0)
        levelBonus = self.levelBonuses.get(attribute, 0)
        equipmentBonus = sum(bonus for _, bonus in self.equipmentBonuses.get(attribute, []))
        boonBonus = sum(bonus for _, bonus in self.boonBonuses.get(attribute, []))
        cursePenalty = sum(penalty for _, penalty in self.cursePenalties.get(attribute, []))   
        override = self.attributeOverrides.get(attribute)
        return override[1] if override is not None else base + levelBonus + equipmentBonus + boonBonus - cursePenalty

    def getAttributeModifier(self, attribute):
        """
        Calculates the modifier for a given attribute score.
        """
        score = self.getAttributeScore(attribute)
        return (score // 2) - 5 # Floor division to round down
    
    def addLevel(self, className):
        if className in AVAILABLE_CLASSES:
            if className not in self.classes:
                self.classes[className] = 1
                self.levelHistory.append((className, 1))
                logMessage("info", f"{self.name} gained their first level in {className}!")

        # Apply saving throw prof for the first level
        class_def = AVAILABLE_CLASSES[className]()
        saving_throws = class_def.getSavingThrowProf()
        for save in saving_throws:
            if save in self.savingThrowProf:
                self.savingThrowProf[save] = True
                logMessage("info", f"Proficiency in '{save}' saving throws applied.")
        
        # Handle skill profs at level 1
        numChoices, availableSkills = class_def.getSkillProfAtLevel(1)
        if numChoices > 0:
            print(f"Choose {numChoices} skill proficiencies from the following list:")
            for i, skill in enumerate(availableSkills, 1):
                print(f"{i}. {skill}")
            chosenSkills = set()
            for i in range(numChoices):
                while True:
                    try:
                        choice = int(input(f"Enter the number for skill {i+1}: "))
                        if 1 <= choice <= len(availableSkills):
                            chosenSkill = availableSkills[choice - 1]
                            if chosenSkill not in chosenSkills:
                                self.applySkillProf(chosenSkill)
                                chosenSkills.add(chosenSkill)
                                logMessage("info", f"Proficiency in '{chosenSkill}' applied.")
                                break
                            else:
                                print(f"You are already proficient in '{chosenSkill}'. Please choose another.")
                        else:
                            print("Invalid input. Please enter a number from the list.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                logMessage("info", "Skill proficiencies chosen.")
        else:
            self.classes[className] += 1
            self.levelHistopry.append((className, self.classes[className]))
            logMessage("info", f"{self.name} gained a level in {className}! They are now level {self.classes[className]}.")
            # Handle skill proficiencies at subsequent levels (if any)
            class_def = AVAILABLE_CLASSES[className]()
            numChoices, availableSkills = class_def.getSkillProfAtLevel(self.classes[className])
            if numChoices > 0:
                print(f"Choose {numChoices} additional skill proficiencies from the following list:")
                for i, skill in enumerate(availableSkills, 1):
                    print(f"{i}. {skill}")
                chosenSkills = set()
                for i in range(numChoices):
                    while True:
                        try:
                            choice = int(input(f"Enter the number for skill {i+1}: "))
                            if 1 <= choice <= len(availableSkills):
                                chosenSkill = availableSkills[choice - 1]
                                if chosenSkill not in self.skills or not self.skills[chosenSkill]:
                                    self.applySkillProf(chosenSkill)
                                    chosenSkills.add(chosenSkill)
                                    logMessage("info", f"Proficiency in '{chosenSkill}' applied.")
                                    break
                                else:
                                    print(f"You are already proficient in '{chosenSkill}'. Please choose another.")
                            else:
                                print("Invalid input. Please enter a number from the list.")
                        except ValueError:
                            print("Invalid input. Please enter a number.")
                logMessage("info", "Skill proficiencies chosen.")
            else:
                logMessage("error", f"Class '{className}' not found.")
            
        
        
    def reduceLevel(self, className, levelsToReduce=1, revertStats=False):
        """
        Reduces the level in a specific class. Can optionally revert level_based stat increases. Possibly useful for rollback of levels, or a curse.
        """
        if className in self.classes and self.classes[className] > 0:
            self.classes[className] -= levelsToReduce
            if self.classes[className] < 0:
                self.classes[className] = 0 # Ensure level doesn't go below 0
            
            #TODO implement log ic to handle level history and potentially revert stats based on the 'revertStats' flag and the level history. This will be more complex.
            logMessage("INFO", f"{self.name}'s level in {className} reduced to {self.classes[className]}.")
            self._updateProfBonus() # Recalculate proficiency bonus on level down
    
    def _updateProfBonus(self):
        """
        Calculates the profieciency bonus based on the character's total level.
        """
        totalLevel = sum(self.classes.values())
        if totalLevel < 5:
            self.profBonus = 2
        elif totalLevel < 9:
            self.profBonus = 3
        elif totalLevel < 13:
            self.profBonus = 4
        elif totalLevel < 17:
            self.profBonus = 5
        else:
            self.profBonus = 6
    
    def applyEquipmentBonus(self, attribute, source, bonus):
        """
        Applies a bonus to an attribute from equipment.
        """
        self.equipmentBonuses[attribute].append((source, bonus))
    
    def removeEquipmentBonus(self, attribute, source, bonus):
        """
        Removes a bonus to an attribute from equipment.
        """
        self.equipmentBonuses[attribute] = [(s, b) for s, b in self.equipmentBonuses[attribute] if s != source or b != bonus]

    def applyBoonBonus(self, attribute, source, bonus):
        self.boonBonuses[attribute].append((source, bonus))

    def removeBoonBonus(self, attribute, source, bonus):
        self.boonBonuses[attribute] = [(s, b) for s, b in self.boonBonuses[attribute] if s != source or b != bonus]

    def applyCursePenalty(self, attribute, source, penalty):
        self.cursePenalties[attribute].append((source, penalty))

    def removeCursePenalty(self, attribute, source, penalty):
        self.cursePenalties[attribute] = [(s, p) for s, p in self.cursePenalties[attribute] if s != source or p != penalty]

    def setAttributeOverride(self, attribute, source, value):
        self.attributeOverrides[attribute] = (source, value)

    def clearAttributeOverride(self, attribute, source):
        if attribute in self.attributeOverrides and self.attributeOverrides[attribute][0] == source:
            del self.attributeOverrides[attribute]
    
    def addFeat(self, featName): #! need to flag back if feat exists on character on add attempt
        if featName not in self.feats:
            self.feats.append(featName)
    
    def hasFeat(self, featName):
        return featName in self.feats
    
    def applySkillProf(self, skill):
        if skill in self.skills:
            self.skills[skill] = True
    
    def removeSkillProf(self, skill):
        if skill in self.skills:
            self.skills[skill] = False
        
    def applySavingThrowProf(self, save):
        if save in self.savingThrowProf:
            self.savingThrowProf[save] = True

    def hasSkillProf(self, skill):
        return self.skills.get(skill, False)
            
    def hasSavingThrowProf(self, save):
        return self.savingThrowProf.get(save, False)
    
    def getSkillCheckBonus(self, skill):
        if self.hasSkillProf(skill):
            ability = self._getSkillAbility(skill)
            return self.getAttributeModifier(ability) + self.profBonus
    
    def getSavingThrowBonus(self, save):
        modifier = self.getAttributeModifier(save)
        if self.hasSavingThrowProf(save):
            return modifier + self.profBonus
        else:
            return modifier
    
    def _getSkillAbility(self, skill):
        """
        Helper function to map skills to their governing abilities.
        """
        skillAbilities = {
            "Athletics": "STR",
            "Acrobatics": "DEX",
            "Sleight of Hand": "DEX",
            "Stealth": "DEX",
            "Arcana": "INT",
            "History": "INT",
            "Investigation": "INT",
            "Nature": "INT",
            "Religion": "INT",
            "Animal Handling": "WIS",
            "Insight": "WIS",
            "Medicine": "WIS",
            "Perception": "WIS",
            "Survival": "WIS",
            "Deception": "CHA",
            "Intimidation": "CHA",
            "Performance": "CHA",
            "Persuasion": "CHA"
        }
        return skillAbilities.get(skill, None)
            

    
#example instantiation:
if __name__ == "__main__":
    # Test Human
    humanCharacter = Character(
        name="Alice",
        race="Human",
        background="Folk Hero",
        alignment="Neutral Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=[]
    )
    print("\n--- Human Test ---")
    print(f"Name: {humanCharacter.name}")
    print(f"Race: {humanCharacter.race}")
    print(f"Base Attributes after racial bonuses: {humanCharacter.baseAttributes}")
    print(f"Racial Traits: {humanCharacter.racialTraits}")
    print(f"Speed: {humanCharacter.speed}")
    print(f"Languages: {humanCharacter.languages}")
    print(f"Size: {humanCharacter.size}")

    # Test Dwarf
    dwarfCharacter = Character(
        name="Borin",
        race="Dwarf",
        background="Guild Artisan",
        alignment="Lawful Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=[]
    )
    print("\n--- Dwarf Test ---")
    print(f"Name: {dwarfCharacter.name}")
    print(f"Race: {dwarfCharacter.race}")
    print(f"Base Attributes after racial bonuses: {dwarfCharacter.baseAttributes}")
    print(f"Racial Traits: {dwarfCharacter.racialTraits}")
    print(f"Speed: {dwarfCharacter.speed}")
    print(f"Languages: {dwarfCharacter.languages}")
    print(f"Size: {dwarfCharacter.size}")
    

    anya_to_level = Character(
        name="AnyaLevelTest",
        race="Half-Elf",
        background="Noble",
        alignment="Chaotic Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=["Lucky"]
    )

    print("\n--- Anya Level Test ---")
    anya_to_level.addLevel("Fighter")
    print(f"Anya's Saving Throw Proficiencies after level 1 Fighter: {anya_to_level.savingThrowProf}")

    anya_to_level.addLevel("Wizard")
    print(f"Anya's Saving Throw Proficiencies after level 1 Wizard: {anya_to_level.savingThrowProf}")
    
    print("\n--- Human Speed Test ---")
    print(f"{humanCharacter.name}'s Speed: {humanCharacter.speed}")
    print(f"{humanCharacter.name}'s Fly Speed: {humanCharacter.flySpeed}")
    print(f"{humanCharacter.name}'s Swim Speed: {humanCharacter.swimSpeed}")
    print(f"{humanCharacter.name}'s Climb Speed: {humanCharacter.climbSpeed}")
    print(f"{humanCharacter.name}'s Burrow Speed: {humanCharacter.burrowSpeed}")

    print("\n--- Dwarf Speed Test ---")
    print(f"{dwarfCharacter.name}'s Speed: {dwarfCharacter.speed}")
    print(f"{dwarfCharacter.name}'s Fly Speed: {dwarfCharacter.flySpeed}")
    print(f"{dwarfCharacter.name}'s Swim Speed: {dwarfCharacter.swimSpeed}")
    print(f"{dwarfCharacter.name}'s Climb Speed: {dwarfCharacter.climbSpeed}")
    print(f"{dwarfCharacter.name}'s Burrow Speed: {dwarfCharacter.burrowSpeed}")