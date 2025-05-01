def addLevel(self, className):
        """
        Increases the level in a specific class.
        """
        self.classes[className] = self.classes.get(className, 0) + 1
        self.levelHistory.append((className, self.classes[className]))
        self._updateProfBonus() # Recalculate proficiency bonus on level up
        #TODO trigger other level-based stat increases and otehr class feature unlocks etc.