_registeredBackgrounds = {}

def registered(cls):
    _registeredBackgrounds[cls.__name__] = cls
    return cls


def sourcebook(bookName):
    def decorator(cls):
        setattr(cls, '_sourcebook', bookName)
        return cls
    return decorator


def getAvailableBackgrounds():
    return _registeredBackgrounds


class Background:
    def __init__(self, name, skillProf=None, toolProf=None, languages=None, equipment=None, features=None):
        self.name = name
        self.skillProf = skillProf if skillProf else []
        self.toolProf = toolProf if toolProf else []
        self.languages = languages if languages else []
        self.equipment = equipment if equipment else []
        self.features = features if features else []


    
#@ Copypastable template system for additional backgrounds
class BaseBackground(Background): # Inherit from the base Background class
    def __init__(self):
        super().__init__(
            name="Your Background Name",
            skillProf=["Skill 1", "Skill 2"], # List of skills
            toolProf=["Tool 1", "Tool 2"], # List of tools (can be empty)
            languages=["Language 1", "Language 2"], # List of languages (can be empty)
            # equipment=["Item 1", "Item 2"], # We'll handle equipment later
            features="Your Background Feature Name" # Brief description of the feature
        )
        
class YourBackgroundName(BaseBackground): # Create a new class for your background
    def __init__(self):
        super().__init__()
        # Override any default values here if needed
        self.name = "Your Specific Background Name"
        self.skillProf = ["Specific Skill 1", "Specific Skill 2"]
        self.toolProf = ["Specific Tool"]
        self.languages = ["Specific Language"]
        self.features = "A unique feature for this background"
        

class _(Background):
    def __init__(self):
        super().__init__(
            name="",
            skillProf=[
                "",
                ""
            ],
            toolProf=[
                "",
                ""
            ],
            languages=[
                "",
                ""
            ],
            equipment=[
                "",
                ""
            ],
            features=[
                "",
                ""
            ]
        )