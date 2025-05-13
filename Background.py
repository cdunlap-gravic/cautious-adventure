_registeredBackgrounds = {}

def registeredBackground(cls):
    _registeredBackgrounds[cls.__name__] = cls
    return cls

class Background:
    def __init__(self, name, skillProf, toolProf=None, languages=None, equipment=None, feature=None):
        self.name = name
        self.skillProf = skillProf
        self.toolProf = toolProf if toolProf else []
        self.languages = languages if languages else []
        self.equipment = equipment if equipment else []
        self.feature = feature

@registeredBackground      
class Noble(Background):
    def __init__(self):
        super().__init__(
            name="Noble",
            skillProf=[
                "History",
                "Persuasion"
            ],
            toolProf=[
                "Gaming set (one type)"
            ],
            languages=[
                "One extra language of your choice"
            ],
            feature="Position of Priviledge"
        )

@registeredBackground
class Criminal(Background):
    def __init__(self):
        super().__init__(
            name="Criminal",
            skillProf=[
                "Deception",
                "Stealth"
            ],
            toolProf=[
                "Gaming set (five types), thieves' tools"
            ],
            languages=[],
            feature="Criminal Contact"
        )
    
#@ Copypastable template system for additional backgrounds
class BaseBackground(Background): # Inherit from the base Background class
    def __init__(self):
        super().__init__(
            name="Your Background Name",
            skillProf=["Skill 1", "Skill 2"], # List of skills
            toolProf=["Tool 1", "Tool 2"], # List of tools (can be empty)
            languages=["Language 1", "Language 2"], # List of languages (can be empty)
            # equipment=["Item 1", "Item 2"], # We'll handle equipment later
            feature="Your Background Feature Name" # Brief description of the feature
        )
        
class YourBackgroundName(BaseBackground): # Create a new class for your background
    def __init__(self):
        super().__init__()
        # Override any default values here if needed
        self.name = "Your Specific Background Name"
        self.skillProf = ["Specific Skill 1", "Specific Skill 2"]
        self.toolProf = ["Specific Tool"]
        self.languages = ["Specific Language"]
        self.feature = "A unique feature for this background"
        
        
def getAvailableBackgrounds():
    return _registeredBackgrounds