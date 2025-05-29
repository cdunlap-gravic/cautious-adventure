from core.types import AbilityScore, CreatureType, Size, FlexConfig, Sourcebooks, RacialTrait, Tools
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
                RacialTrait.DRACONIC_ANCESTRY,
                RacialTrait.DRACONIC_BREATH_WEAPON,
                RacialTrait.DRACONIC_DAMAGE_RESISTANCE
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
                RacialTrait.DWARVEN_SPEED,
                RacialTrait.DARKVISION,
                RacialTrait.DWARVEN_RESILIENCE,
                RacialTrait.DWARVEN_COMBAT_TRAINING,
                RacialTrait.STONE_CUNNING
                
            ],
            toolProf={
                (1, [
                    Tools.SMITH_TOOLS,
                    Tools.BREWERS_SUPPLIES,
                    Tools.MASONS_TOOLS
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
        self.racialTraits.append(RacialTrait.DWARVEN_TOUGHNESS)
     
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Dwarf_Mountain(Dwarf):
    def __init__(self):
        super().__init__()
        self.name="Mountain Dwarf"
        self.abilityBonuses[AbilityScore.STRENGTH]=2
        self.racialTraits.append(RacialTrait.DWARVEN_ARMOR_TRAINING)
        
        
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
                RacialTrait.DARKVISION,
                RacialTrait.KEEN_SENSES,
                RacialTrait.FEY_ANCESTRY,
                RacialTrait.TRANCE
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
        self.racialTraits.remove(RacialTrait.DARKVISION)
        self.racialTraits.extend([
            RacialTrait.SUPERIOR_DARKVISION,
            RacialTrait.SUNLIGHT_SENSITIVITY,
            RacialTrait.DROW_MAGIC,
            RacialTrait.DROW_WEAPON_TRAINING
        ])


@registered
@sourcebook(Sourcebooks.PHB14)
class Elf_High(Elf):
    def __init__(self):
        super().__init__()
        self.name="High Elf"
        self.abilityBonuses[AbilityScore.INTELLIGENCE]=1
        self.racialTraits.extend([
            RacialTrait.ELF_WEAPON_TRAINING,
            RacialTrait.WIZARD_CANTRIP,
            RacialTrait.EXTRA_LANGUAGE
        ])
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Elf_Wood(Elf):
    def __init__(self):
        super().__init__()
        self.name="Wood Elf"
        self.abilityBonuses[AbilityScore.WISDOM]=1
        self.racialTraits.extend([
            RacialTrait.ELF_WEAPON_TRAINING,
            RacialTrait.FLEET_OF_FOOT,
            RacialTrait.MASK_OF_THE_WILD
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
                RacialTrait.DARKVISION,
                RacialTrait.GNOME_CUNNING
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
            RacialTrait.NATURAL_ILLUSIONIST,
            RacialTrait.SPEAK_WITH_SMALL_BEASTS
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
            RacialTrait.ARTIFICERS_LORE,
            RacialTrait.TINKER
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
                RacialTrait.DARKVISION,
                RacialTrait.FEY_ANCESTRY,
                RacialTrait.SKILL_VERSATILITY,
                RacialTrait.EXTRA_LANGUAGE
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
                RacialTrait.DARKVISION,
                RacialTrait.MENACING,
                RacialTrait.RELENTLESS_ENDURANCE,
                RacialTrait.SAVAGE_ATTACKS
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
                RacialTrait.LUCKY,
                RacialTrait.BRAVE,
                RacialTrait.HALFLING_NIMBLENESS
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
        self.racialTraits.append(RacialTrait.NATURALLY_STEALTHY)


@registered
@sourcebook(Sourcebooks.PHB14)
class Halfling_Stout(Halfling):
    def __init__(self):
        super().__init__()
        self.name = "Stout Halfling"
        self.abilityBonuses[AbilityScore.CONSTITUTION]= 1
        self.racialTraits.append(RacialTrait.STOUT_RESILIENCE)



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
                RacialTrait.EXTRA_LANGUAGE
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
                RacialTrait.EXTRA_LANGUAGE,
                RacialTrait.SKILLS, # CHOOSE 1 SKILL PROF
                RacialTrait.FEAT # CHOSE 1 FEAT
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
                RacialTrait.DARKVISION,
                RacialTrait.HELLISH_RESISTANCE,
                RacialTrait.INFERNAL_LEGACY
            ],
            toolProf=[],
            languages=[
                PHB14_Languages.COMMON,
                PHB14_Languages.INFERNAL
            ],
            size=Size.MEDIUM,
            speed=30
        )