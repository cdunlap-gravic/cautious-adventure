from enum import Enum
from dataclasses import dataclass, field
from typing import List

class Ruling(Enum):
    SOURCE = ("Source Book", "This is written and published by WotC as official content.")
    PARTNERED = ("Partnered Content", "This is offically licensed, but may not be as balanced as WoTC content. (although is what they actually publish ever actually balanced???)")
    OTHER = ("Other source", "????")
    HOMEBREW = ("Homebrew", "Listed on 5e.tools or otherwise manually imported here.")
    
class Sourcebooks(Enum):
    AAG = ("Astral Adventurer's Guide")
    AI = ("Acquisitions Incorporated")
    ALCoS = ("Adventurers League: Curse of Strahd")
    ALEE = ("Adventurers League: Elemental Evil")
    ALRoD = ("Adventurers League: Rage of Demons")
    AitFRAVT = ("Adventures in the Forgotten Realms: A Verdant Tomb")
    BAM = ("Boo's Astral Menagerie")
    BGDIA = ("Baldur's Gate: Descent Into Avernus")
    BGG = ("Bigby Presents: Glory of the Giants", Ruling.SOURCE)
    BMT = ("The Book of Many Things")
    BoET = ("Book of Ebon Tides", Ruling.PARTNERED)
    CM = ("Candlekeep Mysteries")
    CoS = ("Curse of Strahd")
    DMG14 = ("Dungeon Master's Guide (2014)", Ruling.SOURCE)
    DMG24 = ("Dungeon Master's Guide (2024)", Ruling.SOURCE)
    DSotDQ = ("Dragonlance: Shadow of the Dragon Queen", Ruling.SOURCE)
    DitLCoT = ("Descent into the Lost Caverns of Tsojcanth")
    DoDk = ("Dungeons of Drakkenheim")
    DoSI = ("Dragons of Stormwreck Isle")
    EEPC = ("Elemental Evil Player's Companion")
    EET = ("Elemental Evil: Trinkets")
    EGW = ("Explorer's Guide to Wildemount")
    ERLW = ("Eberron: Rising from the Last War")
    FM = ("Flee, Mortals!")
    FTD = ("Fizban's Treasury of Dragons")
    GGR = ("Guildmasters' Guide to Ravnica")
    GHLoE = ("Grim Hollow: Lairs of Etharis")
    GHPP = ("Grim Hollow: Player Pack")
    GoS = ("Ghosts of Saltmarsh")
    GotSF = ("Giants of the Star Forge")
    IDRotF = ("Icewind Dale: Rime of the Frostmaiden")
    IMR = ("Infernal Machine Rebuild")
    IllR = ("The Illrigger Revised")
    JttRC = ("Journey through the Radiant Citadel")
    KftGV = ("Keys from the Golden Vault")
    LLK = ("Lost Laboratory of Kwalish")
    LR = ("Locathah Rising")
    LoX = ("Light of Xaryxis")
    MCV3MC = ("Monstrous Compendium Volume 3: Minecraft Creatures")
    MFF = ("Mordenkainen's Fiendish Folio")
    MM14 = ("Monster Manual (2014)")
    MM25 = ("Monster Manual (2025)")
    MOT = ("Mythic Odysseys of Theros")
    MPMM = ("Mordenkainen Presents: Monsters of the Multiverse")
    MTF = ("Mordenkainen's Tome of Foes")
    OGA = ("One Grung Above")
    OotA = ("Out of the Abyss")
    PHB14 = ("Players' Handbook (2014)", Ruling.SOURCE)
    PHB24 = ("Players' Handbook (2024)", Ruling.SOURCE)
    PSA = ("Planar Shift: Amonkhet")
    PSD = ("Planar Shift: Dominaria")
    PSI = ("Planar Shift: Innistrad")
    PSK = ("Planar Shift: Kaladesh")
    PSX = ("Planar Shift: Ixalan")
    PSZ = ("Planar Shift: Zendikar")
    QftIS = ("Quests from the Infinite Staircase")
    SCAG = ("Sword Coast Adventurer's Guide", Ruling.SOURCE)
    SCC = ("Strixhaven: A Curriculum of Chaos")
    SatO = ("Sigil and the Outlands")
    TAP = ("The Talent and Psionics")
    TCE = ("Tasha's Cauldron of Everything", Ruling.SOURCE)
    TDCSR = ("Tal'Dorei Campaign Setting Reborn")
    TGS2 = ("The Griffon's Saddlebag Book 2")
    TLotRR = ("The Lord of the Rings Roleplaying")
    TftS = ("Tales from the Shadows")
    ToA = ("Tomb of Annihilation")
    ToB123 = ("Tome of Beasts 1 (2023 Edition)")
    UAMy = ("Unearthed Arcana: The Mystic Class")
    VGM = ("Volo's Guide to Monsters")
    VRGR = ("Van Richten's Guide to Ravenloft", Ruling.SOURCE)
    WBtW = ("The Wild Beyond the Witchlight")
    WDH = ("Waterdeep: Dragon Heist")
    WDMM = ("Waterdeep: Dungeon of the Mad Mage")
    WEL = ("Where Evil Lives: The MCDM Book of Boss Battles")
    XGE = ("Xanathar's Guide to Everything", Ruling.SOURCE)
    #$ Books that exist, but I don't have 5e.tools's acroynm yet
    #_ = ("Adventure Atlas: The Mortuary")
    #_ = ("Domains of Delight")
    #_ = ("Dungeons & Dragons vs. Rick and Morty: Basic Rules")
    #_ = ("Minsc and Boo's Journal of Villainy")
    #_ = ("Monsterous Compendium Volume 4: Eldraine Creatures")
    #_ = ("Morte's Planar Parade")
    #_ = ("Tarot Deck")
    #_ = ("The Deck of Many Things: Card Reference Guide")
    #_ = ("Thieve's Gallery")
    
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

class CreatureType(Enum):
    ABERRATION = ("Aberration")
    BEAST = ("Beast")
    CELESTIAL = ("Celestial")
    CONSTRUCT = ("Construct")
    DRAGON = ("Dragon")
    ELEMENTAL = ("Elemental")
    FEY = ("Fey")
    FIEND = ("Fiend")
    GIANT = ("Giant")
    HUMANOID = ("Humanoid")
    MONSTROSITY = ("Monstrosity")
    OOZE = ("Ooze")
    PLANT = ("Plant")
    UNDEAD = ("Undead")


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
    
    
