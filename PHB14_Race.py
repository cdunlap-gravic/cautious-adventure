from AbilityScore import AbilityScore
from Size import Size
from newRace import Race, registered, sourcebook

@registered
@sourcebook("PHB'14")
class Dragonborn(Race):
    def __init__(self):
        super().__init__(
            name="Dragonborn",
            creatureType="Humanoid", #TODO ABSTRACT TO ENUM
            abilityBonuses={
                AbilityScore.STRENGTH.value: 2,
                AbilityScore.CHARISMA.value: 1
            },
            racialTraits=[
                "Draconic Ancestry",
                "Breath Weapon",
                "Damage Resistance"
            ],
            toolProf=[],
            languages=[ #TODO ABSTRACT TO ENUM
                "Common",
                "Draconic"
            ],
            size=Size.MEDIUM,
            speed=30
        )

        
@registered
@sourcebook("PHB'14") 
class Dwarf(Race):
    def __init__(self):
        super().__init__(
            name="Dwarf",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.CONSTITUTION.value: 2
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
                "Common",
                "Dwarvish"
            ],
            size=Size.MEDIUM,
            speed=25
        )
   
        
@registered
@sourcebook("PHB'14") 
class Dwarf_Hill(Dwarf):
    def __init__(self):
        super().__init__()
        self.name="Hill Dwarf"
        self.abilityBonuses[AbilityScore.WISDOM.value]=1
        self.racialTraits.append("Dwarven Toughness")
     
        
@registered
@sourcebook("PHB'14")
class Dwarf_Mountain(Dwarf):
    def __init__(self):
        super().__init__()
        self.name="Mountain Dwarf"
        self.abilityBonuses[AbilityScore.STRENGTH.value]=2
        self.racialTraits.append("Dwarven Armor Training")
        
        
@registered
@sourcebook("PHB'14")
class Elf(Race):
    def __init__(self):
        super().__init__(
            name="Elf",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.DEXTERITY.value: 2
            },
            racialTraits=[
                "Darkvision",
                "Keen Senses",
                "Fey Ancestry",
                "Trance"
            ],
            toolProf=[],
            languages=[
                "Common",
                "Elvish"
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook("PHB'14")
class Elf_Drow(Elf):
    def __init__(self):
        super().__init__()
        self.name="Drow Elf"
        self.abilityBonuses[AbilityScore.CHARISMA.value]=1
        self.racialTraits.remove("Darkvision")
        self.racialTraits.extend([
            "Superior Darkvision",
            "Sunlight Sensitivity",
            "Drow Magic",
            "Drow Weapon Training"
        ])


@registered
@sourcebook("PHB'14")
class Elf_High(Elf):
    def __init__(self):
        super().__init__()
        self.name="High Elf"
        self.abilityBonuses[AbilityScore.INTELLIGENCE.value]=1
        self.racialTraits.extend([
            "Elf Weapon Training",
            "Wizard Cantrip",
            "Extra Language"
        ])
        
        
@registered
@sourcebook("PHB'14")
class Elf_Wood(Elf):
    def __init__(self):
        super().__init__()
        self.name="Wood Elf"
        self.abilityBonuses[AbilityScore.WISDOM.value]=1
        self.racialTraits.extend([
            "Elf Weapon Training",
            "Fleet of Foot",
            "Mask of the Wild"
        ])
        self.speed=35
        
        
@registered
@sourcebook("PHB'14")        
class Gnome(Race):
    def __init__(self):
        super().__init__(
            name="Gnome",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.INTELLIGENCE.value: 2
            },
            racialTraits=[
                "Darkvision",
                "Gnome Cunning"
            ],
            toolProf={},
            languages=[
                "Common",
                "Gnomish"
            ],
            size=Size.SMALL,
            speed=25
        )
        
        
@registered
@sourcebook("PHB'14")
class Gnome_Forest(Gnome):
    def __init__(self):
        super().__init__()
        self.name="Forest Gnome"
        self.abilityBonuses[AbilityScore.DEXTERITY.value]=1
        self.racialTraits.extend([
            "Natural Illusionists",
            "Speak with Small Beasts"
        ])


@registered
@sourcebook("PHB'14")
class Gnome_Rock(Gnome):
    def __init__(self):
        super().__init__()
        self.name="Rock Gnome"
        self.abilityBonuses[AbilityScore.CONSTITUTION.value]=1
        self.toolProf.append("Tinker's Tools")
        self.racialTraits.extend([
            "Artificer's Lore",
            "Tinker"
        ])
        
#######################################################################################
#! HOW TO FIX UNIQUE ABI???
#######################################################################################
@registered
@sourcebook("PHB'14")
class Half_Elf(Race):
    def __init__(self):
        super().__init__(
            name="Half-Elf",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.CHARISMA.value: 2,
                "UNIQUE_ABI": 2 # IMPLIES UNIQUE TO EACHOTHER, AND UNIQUE TO CHARISMA. #! ??? HOW TO DO THIS?
            },
            racialTraits=[
                "Darkvision",
                "Fey Ancestry",
                "Skill Versatility",
                "Extra Language"
            ],
            toolProf=[],
            languages=[
                "Common",
                "Elvish"
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook("PHB'14")
class Half_Orc(Race):
    def __init__(self):
        super().__init__(
            name="Half-Orc",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.STRENGTH.value: 2,
                AbilityScore.CONSTITUTION.value: 1
            },
            racialTraits=[
                "Darkvision",
                "Menacing",
                "Relentless Endurance",
                "Savage Attacks"
            ],
            toolProf=[],
            languages=[
                "Common",
                "Orc"
            ],
            size=Size.MEDIUM,
            speed=30
        )    
        
        
@registered
@sourcebook("PHB'14")
class Halfling(Race):
    def __init__(self):
        super().__init__(
            name="Halfling",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.DEXTERITY.value: 2
            },
            racialTraits=[
                "Lucky",
                "Brave",
                "Halfling Nimbleness"
            ],
            toolProf=[],
            languages=[
                "Common",
                "Halfling"
            ],
            size=Size.SMALL,
            speed=25
        )


@registered
@sourcebook("PHB'14")
class Halfling_Lightfoot(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Lightfoot Halfling"
        self.abilityBonuses[AbilityScore.CHARISMA.value]= 1
        self.racialTraits.append("Naturally Stealthy")


@registered
@sourcebook("PHB'14")
class Halfling_Stout(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Stout Halfling"
        self.abilityBonuses[AbilityScore.CONSTITUTION.value]= 1
        self.racialTraits.append("Stout Resilience")



@registered
@sourcebook("PHB'14")
class Human(Race):
    def __init__(self):
        super().__init__(
            name="Human",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.STRENGTH.value: 1,
                AbilityScore.DEXTERITY.value: 1,
                AbilityScore.CONSTITUTION.value: 1,
                AbilityScore.INTELLIGENCE.value: 1,
                AbilityScore.WISDOM.value: 1,
                AbilityScore.CHARISMA.value: 1
            },
            racialTraits=[
                "Extra Language"
            ],
            toolProf=[],
            languages=[
                "Common"
            ],
            size=Size.MEDIUM,
            speed=30
        )
#######################################################################################
#! HOW TO FIX UNIQUE ABI???
#######################################################################################
@registered
@sourcebook("PHB'14")
class Human_Variant(Race):
    def __init__(self):
        super().__init__(
            name="Human (Varient)",
            creatureType="Humanoid",
            abilityBonuses={
                "UNIQUE_ABI": 2 # +1 TO TWO ABIs #! AGAIN, HOW TO DO THIS CLEANLY?
            },
            racialTraits=[
                "Extra Language",
                "Skills", # CHOOSE 1 SKILL PROF
                "Feat" # CHOSE 1 FEAT
            ],
            toolProf=[],
            languages=[
                "Common"
            ],
            size=Size.MEDIUM,
            speed=30
        )


@registered
@sourcebook("PHB'14")
class Tiefling(Race):
    def __init__(self):
        super().__init__(
            name="Tiefling",
            creatureType="Humanoid",
            abilityBonuses={
                AbilityScore.CHARISMA.value: 2,
                AbilityScore.INTELLIGENCE.value: 1
            },
            racialTraits=[
                "Darkvision",
                "Hellish Resistance",
                "Infernal Legacy"
            ],
            toolProf=[],
            languages=[
                "Common",
                "Infernal"
            ],
            size=Size.MEDIUM,
            speed=30
        )