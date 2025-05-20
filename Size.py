# Should probably put this in a more generic module that holds a bunch of these enums, and import from the same module each different enum

from enum import Enum

class Size(Enum):
    TINY = ("Tiny", 2.5)
    SMALL = ("Small", 5)
    MEDIUM = ("Medium", 5)
    LARGE = ("Large", 10)
    HUGE = ("Huge", 15)
    GARGANTUAN = ("Gargantuan", 20)
    # SPECIAL = ("<Special>", 20) #fill in the blank size. defaults to 20, but can be larger.
    
    def __init__(self, name, space):
        self._value_ = name
        self.space = space
        
    def __str__(self):
        return self.value
    
    def __repr__(self):
        return f"Size.{self.name}, takes {self.space}' x {self.space}' area of the board"