class Class:
    def __init__(self, name, hitDice, savingThrowProf, skillProf, levelFeatures):
        """
        Base class for D&D 5e classes.

        Args:
            name (str): The name of the class (e.g., "Fighter", "Wizard").
            hitDice (str): The type of hit die used by the class (e.g., "d10", "d6").
            savingThrowProf (list): A list of saving throw abilities the class is proficient in (e.g., ["strength", "constitution"]).
            skillProf (dict): A dictionary where keys are the number of skill prof to choose,
                                        and values are lists of available skills (e.g., {2: ["athletics", "acrobatics", ... ]}).
            levelFeatures (dict): A dictionary where keys are level numbers and values are lists of features gained at that level.
        """
        self.name = name
        self.hitDice = hitDice
        self.savingThrowProf = savingThrowProf
        self.skillProf = skillProf
        self.levelFeatures = levelFeatures
        
    def getSkillProfAtLevel(self, level):
        """
        Returns the skill prof gained from this class up to the given level.
        This is a simplified approach; in reality, skill choices are made at 1st level.
        We'll refine this later.
        """
        if 1 in self.skillProf:
            return self.skillProf[1]
        return []
    
    def getSavingThrowProf(self):
        """
        Returns the saving throw prof of this class.
        """
        return self.savingThrowProf
    
    def getLevelFeatures(self, level):
        """
        Returns a list of features gained at the specified level.
        """    
        return self.levelFeatures.get(level, [])
    

class Fighter(Class):
    def __init__(self):
        super().__init__(
            name="Fighter",
            hitDice="d10",
            savingThrowProf=[
                "STR", 
                "CON"
                ],
            skillProf={2: [
                "Athletics", 
                "Acrobatics", 
                "Animal Handling", 
                "History", 
                "Insight", 
                "Intimidation", 
                "Perception", 
                "Survival"
                ]},
            levelFeatures={
                1: ["Fighting Style", "Second Wind"],
                2: ["Action Surge"],
                3: ["Martial Archetype"],
                4: ["ASI or Feat", "Martial Versatility (Optional)"],
                5: ["Extra Attack"],
                6: ["ASI or Feat", "Martial Versatility (Optional)"],
                7: ["Martial Archetype Feature"],
                8: ["ASI or Feat", "Martial Versatility (Optional)"],
                9: ["Indomitable"],
                10: ["Martial Archetype Feature"],
                11: ["Extra Attack"],
                12: ["ASI or Feat", "Martial Versatility (Optional)"],
                13: ["Indomitable"],
                14: ["ASI or Feat", "Martial Versatility (Optional)"],
                15: ["Martial Archetype Feature"],
                16: ["ASI or Feat", "Martial Versatility (Optional)"],
                17: ["Action Surge", "Indomitable"],
                18: ["Martial Archetype Feature"],
                19: ["ASI or Feat", "Martial Versatility (Optional)"],
                20: ["Extra Attack"]
            }
            
        )

class Wizard(Class):
    def __init__(self):
        super().__init__(
            name="Wizard",
            hitDice="d6",
            savingThrowProf=[
                "INT", 
                "WIS"
                ],
            skillProf={2: [
                "Arcana", 
                "History", 
                "Insight", 
                "Investigation", 
                "Medicine", 
                "Religion"
                ]},
            levelFeatures={
                1: ["Spellcasting", "Arcane Recovery"],
                2: ["Arcane Tradition"],
                3: ["Cantrip Formulas (Optional)"],
                4: ["ASI or Feat"],
                6: ["Arcane Tradition feature"],
                8: ["ASI or Feat"],
                10: ["Arcane Tradition feature"],
                12: ["ASI or Feat"],
                14: ["Arcane Tradition feature"],
                16: ["ASI or Feat"],
                18: ["Spell Mastery"],
                19: ["ASI or Feat"],
                20: ["Signature Spells"]
            }
        )
