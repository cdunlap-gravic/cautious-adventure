from enum import Enum
from dataclasses import dataclass, field
from typing import List

class Sourcebooks(Enum):
    PHB14 = ("Players' Handbook (2014)")
    MM14 = ("Monster Manual (2014)")
    DMG14 = ("Dungeon Master's Guide (2014)")
    PHB24 = ("Players' Handbook (2024)")
    MM25 = ("Monster Manual (2025)")
    DMG24 = ("Dungeon Master's Guide (2024)")
    volo = ("Volo's Guide to Monsters")
    XGE = ("Xanathar's Guide to Everything")
    MTF = ("Mordenkainen's Tome of Foes")
    AI = ("Acquisitions Incorporated")
    TCE = ("Tasha's Cauldron of Everything")
    FTD = ("Fizban's Treasury of Dragons")
    MPMM = ("Mordenkainen Presents: Monsters of the Multiverse")
    AAG = ("Astral Adventurer's Guide")
    #_ = ("Boo's Astral Menagerie")
    #_ = ("Bigby Presents: Glory of the Giants")
    #_ = ("Morte's Planar Parade")
    SatO = ("Sigil and the Outlands")
    BMT = ("The Book of Many Things")
    #_ = ("The Deck of Many Things: Card Reference Guide")
    SCAG = ("Sword Coast Adventurer's Guide")
    GGR = ("Guildmasters' Guide to Ravnica")
    ERLW = ("Eberron: Rising from the Last War")
    MOT = ("Mythic Odysseys of Theros")
    VRGR = ("Van Richten's Guide to Ravenloft")
    SCC = ("Strixhaven: A Curriculum of Chaos")
    TDCSR = ("Tal'Dorei Campaign Setting Reborn")
    PSZ = ("Planar Shift: Zendikar")
    PSI = ("Planar Shift: Innistrad")
    PSK = ("Planar Shift: Kaladesh")
    PSA = ("Planar Shift: Amonkhet")
    PSX = ("Planar Shift: Ixalan")
    OGA = ("One Grung Above")
    PSD = ("Planar Shift: Dominaria")
    #_ = ("Dungeons & Dragons vs. Rick and Morty: Basic Rules")
    #_ = ("Domains of Delight")
    #_ = ("Minsc and Boo's Journal of Villainy")
    #_ = ("Tarot Deck")
    BoET = ("Book of Ebon Tides")
    #_ = ("Thieve's Gallery")
    TGS2 = ("The Griffon's Saddlebag Book 2")
    #_ = ("Tome of Beasts 1 (2023 Edition)")
    #_ = ("Monsterous Compendium Volume 4: Eldraine Creatures")
    #_ = ("Adventure Atlas: The Mortuary")
    FM = ("Flee, Mortals!")
    WEL = ("Where Evil Lives: The MCDM Book of Boss Battles")
    TAP = ("The Talent and Psionics")
    IllR = ("The Illrigger Revised")
    GHPP = ("Grim Hollow: Player Pack")
    TLotRR = ("The Lord of the Rings Roleplaying")
    TftS = ("Tales from the Shadows")
    LLK = ("Lost Laboratory of Kwalish")
    IDRotF = ("Icewind Dale: Rime of the Frostmaiden")
    GHLoE = ("Grim Hollow: Lairs of Etharis")
    EGW = ("Explorer's Guide to Wildemount")
    DoDk = ("Dungeons of Drakkenheim")
    AitFRAVT = ("Adventures in the Forgotten Realms: A Verdant Tomb")
    LR = ("Locathah Rising")
    DSotDQ = ("Dragonlance: Shadow of the Dragon Queen")
    WBtW = ("The Wild Beyond the Witchlight")
    EEPC = ("Elemental Evil Player's Companion")
    UAMy = ("Unearthed Arcana: The Mystic Class")
    
class AbilityScore(Enum):
    """
    Represents the six core ability scores in D&D 5th Edition,
    with an associated description.
    """
    # Each member has two arguments: the shortName (value) and the description
    STRENGTH = ("STR", "Measures physical power, training, and the extent to which you can exert raw physical force.")
    DEXTERITY = ("DEX", "Measures agility, reflexes, and balance.")
    CONSTITUTION = ("CON", "Measures health, stamina, and vital force.")
    INTELLIGENCE = ("INT", "Measures mental acuity, accuracy of recall, and the ability to reason.")
    WISDOM = ("WIS", "Measures how attuned you are to the world around you and represents perceptiveness and intuition.")
    CHARISMA = ("CHA", "Measures your ability to interact effectively with others through confidence, eloquence, or a commanding presence.")
    FLEX = ("FLEX", "Please choose an ability score to increase by 1.")
    
    def __init__(self, value, description):
        self._value_ = value
        self.description = description

    def __str__(self):
        return self.value

    def __repr__(self):
        return f"AbilityScore.{self.name} ('{self.value}')"

    def fullDescription(self):
        return f"{self.name} ({self.value}): {self.description}"



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
    

class Skill(Enum):
    """
    Represents the 18 core skills in D&D 5th Edition.
    Each skill has a name and a governing ability score.
    """
    ACROBATICS = ("Acrobatics", AbilityScore.DEXTERITY)
    ANIMAL_HANDLING = ("Animal Handling", AbilityScore.WISDOM)
    ARCANA = ("Arcana", AbilityScore.INTELLIGENCE)
    ATHLETICS = ("Athletics", AbilityScore.STRENGTH)
    DECEPTION = ("Deception",AbilityScore.CHARISMA)
    HISTORY = ("History", AbilityScore.WISDOM)
    INSIGHT = ("Insight", AbilityScore.WISDOM)
    INTIMIDATION = ("Intimidation", AbilityScore.CHARISMA)
    INVESTIGATION = ("Investigation", AbilityScore.INTELLIGENCE)
    MEDICINE = ("Medicine", AbilityScore.WISDOM)
    NATURE = ("Nature", AbilityScore.INTELLIGENCE)
    PERCEPTION = ("Perception", AbilityScore.WISDOM)
    PERFORMANCE = ("Performance", AbilityScore.CHARISMA)
    PERSUASION = ("Persuasion", AbilityScore.CHARISMA)
    RELIGION = ("Religion", AbilityScore.INTELLIGENCE)
    SLEIGHT_OF_HAND = ("Sleight of Hand", AbilityScore.DEXTERITY)
    STEALTH = ("Stealth", AbilityScore.DEXTERITY)
    SURVIVAL = ("Survival", AbilityScore.WISDOM)
    
    def __init__(self, name: str, abilityScore: AbilityScore):
        self._value_ = name # The primary string value for the enum member
        self.abilityScore = abilityScore

    def __str__(self):
        return self.value   # Returns "Acrobatics", "Athletics", etc.

    def __repr__(self):
        return f"Skill.{self.name} ('{self.value}', related to {self.abilityScore})"

    @property
    def relatedAbilityShort(self) -> str:
        return self.abilityScore.value


@dataclass(frozen=True)
class FlexConfig:
    count: int = 1
    value: int = 1
    exclude: List[AbilityScore] = field(default_factory=list)