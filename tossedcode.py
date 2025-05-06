def addLevel(self, className):
        """
        Increases the level in a specific class.
        """
        self.classes[className] = self.classes.get(className, 0) + 1
        self.levelHistory.append((className, self.classes[className]))
        self._updateProfBonus() # Recalculate proficiency bonus on level up
        #TODO trigger other level-based stat increases and otehr class feature unlocks etc.
        
        
        
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