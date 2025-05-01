from Class import Fighter, Wizard

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
        self.speed = 0
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
        self.classes[className] = self.classes.get(className, 0) + 1
        self.levelHistory.append((className, self.classes[className]))
        self._updateProfBonus()
        if className in self.classes:
            level = self.classes[className]
            if className == "Fighter" and level == 1:
                fighter = Fighter() # Instantiate the class to get its properties
                for skill in fighter.getSkillProfAtLevel(1): # Simplified for now
                    self.applySkillProf(skill)
                for save in fighter.getSavingThrowProf():
                    self.applySavingThrowProf(save)
            elif className == "Wizard" and level == 1:
                wizard = Wizard()
                for skill in wizard.getSkillProfAtLevel(1): # Simplified for now
                    self.applySkillProf(skill)
                for save in wizard.getSavingThrowProf():
                    self.applySavingThrowProf(save)
        # In the future, we'll need a more robust system for handling skill choices.
        
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
    myCharacter = Character(
        name="Anya",
        race="Half-Elf",
        background="Noble",
        alignment="Chaotic Good",
        baseAttributes={
            "STR": 14, 
            "DEX": 13, 
            "CON": 15, 
            "INT": 10, 
            "WIS": 12, 
            "CHA": 8
            },
        feats=["Lucky"]
    )

    myCharacter.addLevel("Fighter")
    print(f"{myCharacter.name}'s Fighter Level: {myCharacter.classes.get('Fighter', 0)}")
    print(f"{myCharacter.name}'s Saving Throw Proficiencies: {myCharacter.savingThrowProf}")
    print(f"{myCharacter.name}'s Skill Proficiencies: {myCharacter.skills}")
    print(f"{myCharacter.name}'s Athletics Check Bonus: +{myCharacter.getSkillCheckBonus('Athletics')}")
    print(f"{myCharacter.name}'s Stealth Check Bonus: +{myCharacter.getSkillCheckBonus('Stealth')}")
    print(f"{myCharacter.name}'s Strength Save Bonus: +{myCharacter.getSavingThrowBonus('Strength')}")

    myCharacter.addLevel("Wizard")
    print(f"{myCharacter.name}'s Wizard Level: {myCharacter.classes.get('Wizard', 0)}")
    print(f"{myCharacter.name}'s Saving Throw Proficiencies: {myCharacter.savingThrowProf}")
    print(f"{myCharacter.name}'s Skill Proficiencies: {myCharacter.skills}")
    print(f"{myCharacter.name}'s Arcana Check Bonus: +{myCharacter.getSkillCheckBonus('Arcana')}")
    print(f"{myCharacter.name}'s Intelligence Save Bonus: +{myCharacter.getSavingThrowBonus('Intelligence')}")
        