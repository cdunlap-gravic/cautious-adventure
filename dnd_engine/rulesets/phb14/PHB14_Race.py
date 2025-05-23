from core.types import AbilityScore, CreatureType, Size, FlexConfig, Sourcebooks
from core.Race import Race, registered, sourcebook

from PHB14_Types import PHB14_Languages
@registered
@sourcebook(Sourcebooks.PHB14)
class Dragonborn(Race):
    def __init__(self):
        super().__init__(
            name="Dragonborn",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.STRENGTH: 2,
                AbilityScore.CHARISMA: 1
            },
            racialTraits=[
                "Draconic Ancestry",
                "Breath Weapon",
                "Damage Resistance"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.DRACONIC
            ],
            size=Size.MEDIUM,
            speed=30
        )

        
@registered
@sourcebook(Sourcebooks.PHB14)
class Dwarf(Race):
    def __init__(self):
        super().__init__(
            name="Dwarf",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.CONSTITUTION: 2
            },
            racialTraits=[
                "Dwarven Speed",
                "Darkvision",
                "Dwarven Resilience",
                "Dwarven Combat Training",
                "Stonecunning"
                
            ],
            toolProf={
                (1, [
                    "Smith's Tools",
                    "Brewer's Supplies",
                    "Mason's Tools"  
                    ]
                )
            },
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.DWARVISH
            ],
            size=Size.MEDIUM,
            speed=25
        )
   
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Dwarf_Hill(Dwarf):
    def __init__(self):
        super().__init__()
        self.name="Hill Dwarf"
        self.abilityBonuses[AbilityScore.WISDOM]=1
        self.racialTraits.append("Dwarven Toughness")
     
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Dwarf_Mountain(Dwarf):
    def __init__(self):
        super().__init__()
        self.name="Mountain Dwarf"
        self.abilityBonuses[AbilityScore.STRENGTH]=2
        self.racialTraits.append("Dwarven Armor Training")
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Elf(Race):
    def __init__(self):
        super().__init__(
            name="Elf",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.DEXTERITY: 2
            },
            racialTraits=[
                "Darkvision",
                "Keen Senses",
                "Fey Ancestry",
                "Trance"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.ELVISH
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Elf_Drow(Elf):
    def __init__(self):
        super().__init__()
        self.name="Drow Elf"
        self.abilityBonuses[AbilityScore.CHARISMA]=1
        self.racialTraits.remove("Darkvision")
        self.racialTraits.extend([
            "Superior Darkvision",
            "Sunlight Sensitivity",
            "Drow Magic",
            "Drow Weapon Training"
        ])


@registered
@sourcebook(Sourcebooks.PHB14)
class Elf_High(Elf):
    def __init__(self):
        super().__init__()
        self.name="High Elf"
        self.abilityBonuses[AbilityScore.INTELLIGENCE]=1
        self.racialTraits.extend([
            "Elf Weapon Training",
            "Wizard Cantrip",
            "Extra Language"
        ])
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Elf_Wood(Elf):
    def __init__(self):
        super().__init__()
        self.name="Wood Elf"
        self.abilityBonuses[AbilityScore.WISDOM]=1
        self.racialTraits.extend([
            "Elf Weapon Training",
            "Fleet of Foot",
            "Mask of the Wild"
        ])
        self.speed=35
        
        
@registered
@sourcebook(Sourcebooks.PHB14)      
class Gnome(Race):
    def __init__(self):
        super().__init__(
            name="Gnome",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.INTELLIGENCE: 2
            },
            racialTraits=[
                "Darkvision",
                "Gnome Cunning"
            ],
            toolProf={},
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.GNOMISH
            ],
            size=Size.SMALL,
            speed=25
        )
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Gnome_Forest(Gnome):
    def __init__(self):
        super().__init__()
        self.name="Forest Gnome"
        self.abilityBonuses[AbilityScore.DEXTERITY]=1
        self.racialTraits.extend([
            "Natural Illusionists",
            "Speak with Small Beasts"
        ])


@registered
@sourcebook(Sourcebooks.PHB14)
class Gnome_Rock(Gnome):
    def __init__(self):
        super().__init__()
        self.name="Rock Gnome"
        self.abilityBonuses[AbilityScore.CONSTITUTION]=1
        self.toolProf.append("Tinker's Tools")
        self.racialTraits.extend([
            "Artificer's Lore",
            "Tinker"
        ])
        

@registered
@sourcebook(Sourcebooks.PHB14)
class Half_Elf(Race):
    def __init__(self):
        super().__init__(
            name="Half-Elf",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.CHARISMA: 2,
                AbilityScore.FLEX: FlexConfig(
                    count=2,
                    value=1,
                    exclude=[AbilityScore.CHARISMA]
                )
            },
            racialTraits=[
                "Darkvision",
                "Fey Ancestry",
                "Skill Versatility",
                "Extra Language"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.ELVISH
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Half_Orc(Race):
    def __init__(self):
        super().__init__(
            name="Half-Orc",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.STRENGTH: 2,
                AbilityScore.CONSTITUTION: 1
            },
            racialTraits=[
                "Darkvision",
                "Menacing",
                "Relentless Endurance",
                "Savage Attacks"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.ORC
            ],
            size=Size.MEDIUM,
            speed=30
        )    
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Halfling(Race):
    def __init__(self):
        super().__init__(
            name="Halfling",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.DEXTERITY: 2
            },
            racialTraits=[
                "Lucky",
                "Brave",
                "Halfling Nimbleness"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.HALFLING
            ],
            size=Size.SMALL,
            speed=25
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Halfling_Lightfoot(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Lightfoot Halfling"
        self.abilityBonuses[AbilityScore.CHARISMA]= 1
        self.racialTraits.append("Naturally Stealthy")


@registered
@sourcebook(Sourcebooks.PHB14)
class Halfling_Stout(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Stout Halfling"
        self.abilityBonuses[AbilityScore.CONSTITUTION]= 1
        self.racialTraits.append("Stout Resilience")



@registered
@sourcebook(Sourcebooks.PHB14)
class Human(Race):
    def __init__(self):
        super().__init__(
            name="Human",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.STRENGTH: 1,
                AbilityScore.DEXTERITY: 1,
                AbilityScore.CONSTITUTION: 1,
                AbilityScore.INTELLIGENCE: 1,
                AbilityScore.WISDOM: 1,
                AbilityScore.CHARISMA: 1
            },
            racialTraits=[
                "Extra Language"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON
            ],
            size=Size.MEDIUM,
            speed=30
        )

@registered
@sourcebook(Sourcebooks.PHB14)
class Human_Variant(Race):
    def __init__(self):
        super().__init__(
            name="Human (Varient)",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.FLEX: FlexConfig(count=2,value=1)
            },
            racialTraits=[
                "Extra Language",
                "Skills", # CHOOSE 1 SKILL PROF
                "Feat" # CHOSE 1 FEAT
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Tiefling(Race):
    def __init__(self):
        super().__init__(
            name="Tiefling",
            creatureType=CreatureType.HUMANOID,
            abilityBonuses={
                AbilityScore.CHARISMA: 2,
                AbilityScore.INTELLIGENCE: 1
            },
            racialTraits=[
                "Darkvision",
                "Hellish Resistance",
                "Infernal Legacy"
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.INFERNAL
            ],
            size=Size.MEDIUM,
            speed=30
        )