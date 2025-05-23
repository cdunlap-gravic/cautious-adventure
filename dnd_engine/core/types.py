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


class DamageType(Enum):
    ACID = ("Acid", "ACD", "The corrosive spray of a black dragon's breath and the dissolving enzymes secreted by a black pudding deal acid damage.")
    BLUDGEONING = ("Bludgeoning", "BLD", "Blunt force attacks—hammers, falling, constriction, and the like—deal bludgeoning damage.")
    COLD = ("Cold", "CLD", "The infernal chill radiating from an ice devil's spear and the frigid blast of a white dragon's breath deal cold damage.")
    FIRE = ("Fire", "FIR", "Red dragons breathe fire, and many spells conjure flames to deal fire damage.")
    FORCE = ("Force", "FRC", "Force is pure magical energy focused into a damaging form. Most effects that deal force damage are spells, including magic missile and spiritual weapon.")
    LIGHTNING = ("Lightning", "LTN", "A lightning bolt spell and a blue dragon's breath deal lightning damage.")
    NECROTIC = ("Necrotic", "NEC", "Necrotic damage, dealt by certain undead and some spells, withers matter and even the soul.")
    PIERCING = ("Piercing", "PRC", "Puncturing and impaling attacks, including spears and monsters' bites, deal piercing damage.")
    POISON = ("Poison", "PSN", "Venomous stings and the toxic gas of a green dragon's breath deal poison damage.")
    PSYCHIC = ("Psychic", "PSY", "Mental abilities such as a mind flayer's psionic blast deal psychic damage.")
    RADIANT = ("Radiant", "RDN", "Radiant damage, dealt by a cleric's flame strike spell or an angel's smiting weapon, sears the flesh like fire and overloads the spirit with power.")
    SLASHING = ("Slashing", "SLS", "Swords, axes, and monsters' claws deal slashing damage.")
    THUNDER = ("Thunder", "THN", "A concussive burst of sound, such as the effect of the thunderwave spell, deals thunder damage.")


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

class TraitCategory(Enum):
    SENSE = "Sense"               # e.g., Darkvision, Superior Darkvision
    PROFICIENCY = "Proficiency"   # e.g., Elf Weapon Training, Keen Senses, Menacing
    DEFENSE = "Defense"           # e.g., Dwarven Resilience, Hellish Resistance, Relentless Endurance, Brave, Stout Resilience
    MOVEMENT = "Movement"         # e.g., Dwarven Speed, Fleet of Foot, Halfling Nimbleness
    MAGIC = "Magic"               # e.g., Drow Magic, Infernal Legacy, Wizard Cantrip, Natural Illusionist
    UTILITY = "Utility"           # e.g., Trance, Stonecunning, Tinker, Speak with Small Beasts, Mask of the Wild
    SPECIAL_ABILITY = "Special Ability" # e.g., Breath Weapon, Savage Attacks, Gnome Cunning, Lucky
    CHOICE = "Choice"             # e.g., Extra Language, Skill Versatility, Skills, Feat
    OTHER = "Other"               # For anything that doesn't fit neatly (rare)

    def __str__(self): return self.value
    def __repr__(self): return f"{self.__class__.__name__}.{self.name}"

class RacialTrait(Enum):
    # DWARF
    DWARVEN_TOUGHNESS = (
        "Dwarven Toughness", TraitCategory.DEFENSE,
        "Your hit point maximum increases by 1, and it increases by 1 every time you gain a level."
    )
    DWARVEN_ARMOR_TRAINING = (
        "Dwarven Armor Training", TraitCategory.DEFENSE,
        "You have proficiency with light and medium armor."
    )
    DWARVEN_RESILIENCE = (
        "Dwarven Resilience", TraitCategory.DEFENSE,
        "You have advantage on saving throws against poison, and you have resistance against poison damage."
    )
    DWARVEN_COMBAT_TRAINING = (
        "Dwarven Combat Training", TraitCategory.PROFICIENCY,
        "You have proficiency with the battleaxe, handaxe, light hammer, and warhammer."
    )
    STONE_CUNNING = (
        "Stonecunning", TraitCategory.UTILITY,
        "Whenever you make an Intelligence (History) check related to the origin of stonework, you are considered proficient in the History skill and add double your proficiency bonus to the check, instead of your normal proficiency bonus."
    )
    DWARVEN_SPEED = (
        "Dwarven Speed", TraitCategory.MOVEMENT,
        "Your speed is not reduced by wearing heavy armor."
    )

    # ELF
    DARKVISION = (
        "Darkvision", TraitCategory.SENSE,
        "You can see in dim light within 60 feet of you as if it were bright light, and in darkness as if it were dim light. You can’t discern color in darkness, only shades of gray."
    )
    SUPERIOR_DARKVISION = (
        "Superior Darkvision", TraitCategory.SENSE,
        "Your darkvision has a radius of 120 feet."
    )
    SUNLIGHT_SENSITIVITY = (
        "Sunlight Sensitivity",
        "You have disadvantage on attack rolls and on Wisdom (Perception) checks that rely on sight when you, the target of your attack, or whatever you are trying to perceive is in direct sunlight."
    )
    DROW_MAGIC = (
        "Drow Magic",
        "You know the 'Dancing Lights' cantrip. When you reach 3rd level, you can cast 'Faerie Fire' once with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can cast 'Darkness' once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
    )
    DROW_WEAPON_TRAINING = (
        "Drow Weapon Training",
        "You have proficiency with rapiers, shortswords, and hand crossbows."
    )
    KEEN_SENSES = (
        "Keen Senses", TraitCategory.PROFICIENCY,
        "You have proficiency in the Perception skill."
    )
    FEY_ANCESTRY = (
        "Fey Ancestry", TraitCategory.DEFENSE,
        "You have advantage on saving throws against being charmed, and magic can’t put you to sleep."
    )
    TRANCE = (
        "Trance", TraitCategory.UTILITY,
        "Your kind don't need to sleep. Instead, you meditate deeply, remaining semiconscious, for 4 hours a day. (The Common word for this meditation is 'trance.') While meditating, you can dream after a fashion; such dreams are actually mental exercises that have become reflexive through years of practice. After resting in this way, you gain the same benefit that a human does from 8 hours of sleep."
    )
    ELF_WEAPON_TRAINING = (
        "Elf Weapon Training",
        "You have proficiency with the longsword, shortsword, shortbow, and longbow."
    )
    WIZARD_CANTRIP = (
        "Wizard Cantrip",
        "You know one cantrip of your choice from the wizard spell list. Intelligence is your spellcasting ability for it."
    )
    EXTRA_LANGUAGE = (
        "Extra Language",
        "You can speak, read, and write one extra language of your choice."
    )
    FLEET_OF_FOOT = (
        "Fleet of Foot",
        "Your base walking speed increases to 35 feet."
    )
    MASK_OF_THE_WILD = (
        "Mask of the Wild",
        "You can attempt to hide even when you are only lightly obscured by foliage, heavy rain, falling snow, mist, or other natural phenomena."
    )

    # DRAGONBORN
    DRACONIC_ANCESTRY = (
        "Draconic Ancestry", TraitCategory.SPECIAL_ABILITY,
        "You have draconic ancestry. Choose one type of dragon from the Draconic Ancestry table. Your breath weapon and damage resistance are determined by the dragon type, as shown in the table."
    )
    DRACONIC_BREATH_WEAPON = (
        "Breath Weapon", TraitCategory.SPECIAL_ABILITY,
        "You can use your action to exhale destructive energy. Your Draconic Ancestry determines the size, shape, and damage type of the exhalation. When you use your breath weapon, each creature in the area of the exhalation must make a saving throw, the type of which is determined by your Draconic Ancestry. The DC for this saving throw equals 8 + your Constitution modifier + your proficiency bonus. A creature takes 2d6 damage on a failed save, and half as much damage on a successful one. The damage increases to 3d6 at 6th level, 4d6 at 11th level, and 5d6 at 16th level. After you use your breath weapon, you can’t use it again until you complete a short or long rest."
    )
    DRACONIC_DAMAGE_RESISTANCE = (
        "Damage Resistance", TraitCategory.DEFENSE,
        "You have resistance to the damage type associated with your Draconic Ancestry."
    )

    # GNOME
    GNOME_CUNNING = (
        "Gnome Cunning",
        "You have advantage on all Intelligence, Wisdom, and Charisma saving throws against magic."
    )
    NATURAL_ILLUSIONIST = (
        "Natural Illusionist",
        "You know the 'Minor Illusion' cantrip. Intelligence is your spellcasting ability for it."
    )
    SPEAK_WITH_SMALL_BEASTS = (
        "Speak with Small Beasts",
        "Through sounds and gestures, you can communicate simple ideas with Small or smaller beasts. Forest gnomes love animals and often keep them as pets."
    )
    ARTIFICERS_LORE = (
        "Artificer's Lore",
        "Whenever you make an Intelligence (History) check related to magic items, alchemical objects, or technological devices, you can add twice your proficiency bonus, instead of any proficiency bonus you normally apply."
    )
    TINKER = (
        "Tinker",
        "You have proficiency with artisan's tools (tinker's tools). Using those tools, you can spend 1 hour and 10 gp worth of materials to construct a Tiny clockwork device (AC 5, 1 hp). The device ceases to function after 24 hours (unless you spend 1 hour repairing it to keep it functioning), or when you use your action to dismantle it. You can have up to three such devices active at a time. When you create the device, choose one of the following options: ... (Full text is long, this is truncated example)"
    )

    # HALF-ELF
    SKILL_VERSATILITY = (
        "Skill Versatility",
        "You gain proficiency in two skills of your choice."
    )

    # HALF-ORC
    MENACING = (
        "Menacing",
        "You gain proficiency in the Intimidation skill."
    )
    RELENTLESS_ENDURANCE = (
        "Relentless Endurance",
        "When you are reduced to 0 hit points but not killed outright, you can drop to 1 hit point instead. You can't use this feature again until you finish a long rest."
    )
    SAVAGE_ATTACKS = (
        "Savage Attacks",
        "When you score a critical hit with a melee weapon attack, you can roll one of the weapon’s damage dice one additional time and add it to the extra damage of the critical hit."
    )

    # HALFLING
    LUCKY = (
        "Lucky",
        "When you roll a 1 on an attack roll, ability check, or saving throw, you can reroll the die and must use the new roll."
    )
    BRAVE = (
        "Brave",
        "You have advantage on saving throws against being frightened."
    )
    HALFLING_NIMBLENESS = (
        "Halfling Nimbleness",
        "You can move through the space of any creature that is of a size larger than yours."
    )
    NATURALLY_STEALTHY = (
        "Naturally Stealthy",
        "You can attempt to hide even when you are obscured only by a creature that is at least one size larger than you."
    )
    STOUT_RESILIENCE = (
        "Stout Resilience",
        "You have advantage on saving throws against poison, and you have resistance to poison damage."
    )

    # HUMAN (Variant)
    SKILLS = (
        "Skills", # CHOOSE 1 SKILL PROF
        "You gain proficiency in one skill of your choice."
    )
    FEAT = (
        "Feat", # CHOOSE 1 FEAT
        "You gain one feat of your choice."
    )

    # TIEFLING
    HELLISH_RESISTANCE = (
        "Hellish Resistance",
        "You have resistance to fire damage."
    )
    INFERNAL_LEGACY = (
        "Infernal Legacy",
        "You know the 'Thaumaturgy' cantrip. When you reach 3rd level, you can cast 'Hellish Rebuke' once as a 2nd-level spell with this trait and regain the ability to do so when you finish a long rest. When you reach 5th level, you can also cast 'Darkness' once with this trait and regain the ability to do so when you finish a long rest. Charisma is your spellcasting ability for these spells."
    )

    # Properties to access the components
    @property
    def name(self):
        """Returns the display name of the racial trait."""
        return self.value[0]

    @property
    def description(self):
        """Returns the official source description of the racial trait."""
        return self.value[1]

    def __str__(self):
        """Allows printing the enum member to get its primary name."""
        return self.name

    def __repr__(self):
        """For debugging, shows enum member name and its display name."""
        return f"{self.__class__.__name__}.{self.name}"


@dataclass(frozen=True)
class FlexConfig:
    count: int = 1
    value: int = 1
    exclude: List[AbilityScore] = field(default_factory=list)
    
    
