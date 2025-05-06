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
                
                
                
                
                self.classes[className] = self.classes.get(className, 0) + 1
        self.levelHistory.append((className, self.classes[className]))
        self._updateProfBonus()
        
        level = self.classes[className]
        
        #@ Definining LV1 choices, ie skill profs etc. Needed for character creation and first level in multiclassing in all systems
        if level == 1:
            classDefinition = AVAILABLE_CLASSES.get(className)
            if classDefinition:
                instance = classDefinition()
                numChoices, availableSkills = instance.getSkillProfAtLevel(1)
                if numChoices > 0:
                    print(f"\n{self.name} gained their first level in {className}!")
                    print(f"Choose {numChoices} skill proficiencies from the following list:")
                    for i, skill in enumerate(availableSkills):
                        print(f"{i + 1}. {skill}")
                        
                    chosenSkills = []
                    while len(chosenSkills) < numChoices:
                        choice = input(f"Enter the number for skill {len(chosenSkills) + 1}: ").strip()
                        if choice.isdigit():
                            index = int(choice) - 1
                            if 0 <= index < len(availableSkills):
                                skill = availableSkills[index]
                                if skill not in self.skills or not self.skills[skill]:
                                    self.applySkillProf(skill)
                                    chosenSkills.append(skill)
                                    print(f"Proficiency in '{skill}' applied.")
                                else:
                                    print(f"You are already proficient in '{skill}'. Please choose another.")
                            else:
                                print("Invalid choice. Please enter a number from the list.")
                        else:
                            print("Invalid input. Please enter a number.")
                    print("Skill proficiencies chosen.")
                
                # Apply saving throw proficiencies for the first level
                for save in instance.getSavingThrowProf():
                    self.applySavingThrowProf(save)
            
            # For subsequent levels or other classes, we'll add more logic here later
        elif className in AVAILABLE_CLASSES and level >= 1:
            instance = AVAILABLE_CLASSES[className]()
            for save in instance.getSavingThrowProf():
                self.applySavingThrowProf(save)