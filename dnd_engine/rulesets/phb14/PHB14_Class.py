# STANDARD IMPORTS FOR CLASS SETS
from core.types import AbilityScore, Skill, Sourcebooks, Tools, Weapons, WeaponCategory, Armor, ArmorCategory, classFeature

from core.Class import Class, registered, sourcebook
from core.SpellSlotTree import FullCastTree, HalfCastTree, PactCastTree

# RULEBOOK SPECIFIC IMPORTS
from PHB14_EquipmentSets import *


#? So how do we want to handle extras like rage count, or rage damage? Extra table?
#? And how do we handle multiclass requirements? Lets at least populate out the rest first...
@registered
@sourcebook(Sourcebooks.PHB14)
class Barbarian(Class):
    def __init__(self):
        super().__init__(
            name="Barbarian",
            hitDie=12,
            savingThrowProf=[
                AbilityScore.STRENGTH,
                AbilityScore.CONSTITUTION
            ],
            skillProf={
                2: [
                    Skill.ANIMAL_HANDLING,
                    Skill.ATHLETICS,
                    Skill.INTIMIDATION,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.SURVIVAL
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                WeaponCategory.MARTIAL
            ],
            toolProf=[],
            armorProf=[
                ArmorCategory.LIGHT,
                ArmorCategory.MEDIUM,
                ArmorCategory.SHIELDS
            ],
            startingEquipment=BarbarianSet,
            levelFeatures={
                1: [classFeature.RAGE, classFeature.UNARMORED_DEFENSE],
                2: [classFeature.DANGER_SENSE, classFeature.RECKLESS_ATTACK],
                3: [classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI],
                5: [classFeature.EXTRA_ATTACK, classFeature.FAST_MOVEMENT],
                6: [classFeature.SUBCLASS_FEATURE],
                7: [classFeature.FERAL_INSTINCT],
                8: [classFeature.ASI],
                9: [classFeature.BRUTAL_CRITICAL],
                10: [classFeature.SUBCLASS_FEATURE],
                11: [classFeature.RELENTLESS_RAGE],
                12: [classFeature.ASI],
                13: [classFeature.BRUTAL_CRITICAL],
                14: [classFeature.SUBCLASS_FEATURE],
                15: [classFeature.PERSISTANT_RAGE],
                16: [classFeature.ASI],
                17: [classFeature.BRUTAL_CRITICAL],
                18: [classFeature.INDOMITABLE_MIGHT],
                19: [classFeature.ASI],
                20: [classFeature.CLASS_CAPSTONE]
            }
        )
@registered
@sourcebook(Sourcebooks.PHB14)
class Bard(Class):
    def __init__(self):
        super().__init__(
            name="Bard",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.DEXTERITY,
                AbilityScore.CHARISMA
            ],
            skillProf={
                3: [
                    Skill.ATHLETICS,
                    Skill.ACROBATICS,
                    Skill.SLEIGHT_OF_HAND,
                    Skill.STEALTH,
                    Skill.ARCANA,
                    Skill.HISTORY,
                    Skill.INVESTIGATION,
                    Skill.NATURE,
                    Skill.RELIGION,
                    Skill.ANIMAL_HANDLING,
                    Skill.INSIGHT,
                    Skill.MEDICINE,
                    Skill.PERCEPTION,
                    Skill.SURVIVAL,
                    Skill.DECEPTION,
                    Skill.INTIMIDATION,
                    Skill.PERFORMANCE,
                    Skill.PERSUASION
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                Weapons.CROSSBOWS_HAND,
                Weapons.LONGSWORDS,
                Weapons.RAPIERS,
                Weapons.SHORTSWORDS
            ],
            toolProf=[Tools.MUSICAL_INSTRUMENT, Tools.MUSICAL_INSTRUMENT, Tools.MUSICAL_INSTRUMENT], # We'll just figure this one out later...
            armorProf=[
                ArmorCategory.LIGHT
            ],
            startingEquipment=None,
            levelFeatures={
                1: [classFeature.BARDIC_INSPIRATION, classFeature.SPELLCASTING],
                2: [classFeature.JACK_OF_ALL_TRADES, classFeature.SONG_OF_REST],
                3: [classFeature.SUBCLASS_CHOICE, classFeature.EXPERTISE],
                4: [classFeature.ASI],
                5: [classFeature.BARDIC_INSPIRATION, classFeature.FONT_OF_INSPIRATION],
                6: [classFeature.COUNTERCHARM, classFeature.SUBCLASS_FEATURE],
                7: [],
                8: [classFeature.ASI],
                9: [classFeature.SONG_OF_REST],
                10: [classFeature.BARDIC_INSPIRATION, classFeature.EXPERTISE, classFeature.MAGICAL_SECRETS],
                11: [],
                12: [classFeature.ASI],
                13: [classFeature.SONG_OF_REST],
                14: [classFeature.MAGICAL_SECRETS, classFeature.SUBCLASS_FEATURE],
                15: [classFeature.BARDIC_INSPIRATION],
                16: [classFeature.ASI],
                17: [classFeature.SONG_OF_REST],
                18: [classFeature.MAGICAL_SECRETS],
                19: [classFeature.ASI],
                20: [classFeature.SUPERIOR_INSPIRATION]
            },
            spellSlotTree=FullCastTree,
            cantripsKnownAtLevel={
                1: 2,
                2: 2,
                3: 2,
                4: 3,
                5: 3,
                6: 3,
                7: 3,
                8: 3,
                9: 3,
                10: 4,
                11: 4,
                12: 4,
                13: 4,
                14: 4,
                15: 4,
                16: 4,
                17: 4,
                18: 4,
                19: 4,
                20: 4
            },
            spellsKnownAtLevel={
                1: 4,
                2: 5,
                3: 6,
                4: 7,
                5: 8,
                6: 9,
                7: 10,
                8: 11,
                9: 12,
                10: 14,
                11: 15,
                12: 15,
                13: 16,
                14: 18,
                15: 19,
                16: 19,
                17: 20,
                18: 22,
                19: 22,
                20: 22
            },
        )
        
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Cleric(Class):
    def __init__(self):
        super().__init__(
            name="Cleric",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.WISDOM,
                AbilityScore.CHARISMA
            ],
            skillProf={
                2: [
                    Skill.HISTORY,
                    Skill.INSIGHT,
                    Skill.MEDICINE,
                    Skill.PERSUASION,
                    Skill.RELIGION #COME ONNNNN why not pick this??? You're a cleric for godssake! (see what I did there? :P)
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE
            ],
            toolProf=[],
            armorProf=[
                ArmorCategory.LIGHT, 
                ArmorCategory.MEDIUM, 
                ArmorCategory.SHIELDS
            ],
            startingEquipment=ClericSet,
            levelFeatures={
                1: [classFeature.SPELLCASTING, classFeature.SUBCLASS_CHOICE],
                2: [classFeature.CHANNEL_DIVINITY, classFeature.SUBCLASS_FEATURE],
                3: [],
                4: [classFeature.ASI],
                5: [classFeature.DESTROY_UNDEAD],
                6: [classFeature.CHANNEL_DIVINITY, classFeature.SUBCLASS_FEATURE],
                7: [],
                8: [classFeature.ASI, classFeature.DESTROY_UNDEAD, classFeature.SUBCLASS_FEATURE],
                9: [],
                10: [classFeature.DIVINE_INTERVENTION],
                11: [classFeature.DESTROY_UNDEAD],
                12: [classFeature.ASI],
                13: [],
                14: [classFeature.DESTROY_UNDEAD],
                15: [],
                16: [classFeature.ASI],
                17: [classFeature.DESTROY_UNDEAD, classFeature.SUBCLASS_FEATURE],
                18: [classFeature.CHANNEL_DIVINITY],
                19: [classFeature.ASI],
                20: [classFeature.DIVINE_INTERVENTION]
            },
            spellSlotTree=FullCastTree,
            cantripsKnownAtLevel={
                1: 3,
                2: 3,
                3: 3,
                4: 4,
                5: 4,
                6: 4,
                7: 4,
                8: 4,
                9: 4,
                10: 5,
                11: 5,
                12: 5,
                13: 5,
                14: 5,
                15: 5,
                16: 5,
                17: 5,
                18: 5,
                19: 5,
                20: 5
            }
        )

@registered
@sourcebook(Sourcebooks.PHB14)
class Druid(Class):
    def __init__(self):
        super().__init__(
            name="Druid",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.INTELLIGENCE,
                AbilityScore.WISDOM
            ],
            skillProf={
                2: [
                    Skill.ARCANA,
                    Skill.ANIMAL_HANDLING,
                    Skill.INSIGHT,
                    Skill.MEDICINE,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.RELIGION,
                    Skill.SURVIVAL
                ]
            },
            weaponProf=[
                Weapons.CLUBS,
                Weapons.DAGGERS, 
                Weapons.DARTS,
                Weapons.JAVALINS,
                Weapons.MACES,
                Weapons.QUARTERSTAVES,
                Weapons.SCIMATARS,
                Weapons.SICKLES,
                Weapons.SLINGS,
                Weapons.SPEARS
            ],
            toolProf=[Tools.HERBALISM_KIT],
            armorProf=[
                ArmorCategory.LIGHT, 
                ArmorCategory.MEDIUM, 
                ArmorCategory.SHIELDS,
                "Exclude Metal" # Yeah no fuck that rule. This is stupid.
            ],
            startingEquipment=DruidSet,
            levelFeatures={
                1: [classFeature.DRUIDIC, classFeature.SPELLCASTING],
                2: [classFeature.WILD_SHAPE, classFeature.SUBCLASS_CHOICE],
                3: [],
                4: [classFeature.WILD_SHAPE, classFeature.ASI],
                5: [],
                6: [classFeature.SUBCLASS_FEATURE],
                7: [],
                8: [classFeature.WILD_SHAPE, classFeature.ASI],
                9: [],
                10: [classFeature.SUBCLASS_FEATURE],
                11: [],
                12: [classFeature.ASI],
                13: [],
                14: [classFeature.SUBCLASS_FEATURE],
                15: [],
                16: [classFeature.ASI],
                17: [],
                18: [classFeature.TIMELESS_BODY, classFeature.BEAST_SPELLS],
                19: [classFeature.ASI],
                20: [classFeature.ARCHDRUID]
            },
            spellSlotTree=FullCastTree,
            cantripsKnownAtLevel={
                1: 2,
                2: 2,
                3: 2,
                4: 3,
                5: 3,
                6: 3,
                7: 3,
                8: 3,
                9: 3,
                10: 4,
                11: 4,
                12: 4,
                13: 4,
                14: 4,
                15: 4,
                16: 4,
                17: 4,
                18: 4,
                19: 4,
                20: 4 
            }
        )
      
@registered
@sourcebook(Sourcebooks.PHB14)
class Fighter(Class):
    def __init__(self):
        super().__init__(
            name="Fighter",
            hitDie=10, # d10
            savingThrowProf=[
                AbilityScore.STRENGTH,
                AbilityScore.CONSTITUTION
            ],
            skillProf={
                2: [
                    Skill.ACROBATICS,
                    Skill.ANIMAL_HANDLING,
                    Skill.ATHLETICS,
                    Skill.HISTORY,
                    Skill.INSIGHT,
                    Skill.INTIMIDATION,
                    Skill.PERCEPTION,
                    Skill.SURVIVAL
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                WeaponCategory.MARTIAL
            ],
            toolProf=[],
            armorProf=[
                ArmorCategory.LIGHT, 
                ArmorCategory.MEDIUM,
                ArmorCategory.HEAVY,
                ArmorCategory.SHIELDS
            ],
            startingEquipment=FighterSet,
            levelFeatures={
                1: [classFeature.FIGHTING_STYLE, classFeature.SECOND_WIND],
                2: [classFeature.ACTION_SURGE],
                3: [classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                5: [classFeature.EXTRA_ATTACK],
                6: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                7: [classFeature.SUBCLASS_FEATURE],
                8: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                9: [classFeature.INDOMITABLE],
                10: [classFeature.SUBCLASS_FEATURE],
                11: [classFeature.EXTRA_ATTACK],
                12: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                13: [classFeature.INDOMITABLE],
                14: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                15: [classFeature.SUBCLASS_FEATURE],
                16: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                17: [classFeature.ACTION_SURGE, classFeature.INDOMITABLE],
                18: [classFeature.SUBCLASS_FEATURE],
                19: [classFeature.ASI, classFeature.SUBCLASS_RESPEC],
                20: [classFeature.EXTRA_ATTACK]
            }
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Monk(Class):
    def __init__(self):
        super().__init__(
            name="Monk",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.STRENGTH,
                AbilityScore.DEXTERITY
            ],
            skillProf={
                2: [
                    Skill.ACROBATICS,
                    Skill.ATHLETICS,
                    Skill.HISTORY,
                    Skill.INSIGHT,
                    Skill.RELIGION,
                    Skill.STEALTH
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                Weapons.SHORTSWORDS
            ],
            toolProf={
                1: [
                    Tools.ARTISANS_TOOLS,
                    Tools.MUSICAL_INSTRUMENT
                ]
            },
            armorProf=[],
            startingEquipment=MonkSet,
            levelFeatures={
                1: [classFeature.UNARMORED_DEFENSE, classFeature.MARTIAL_ARTS],
                2: [classFeature.KI, classFeature.UNARMORED_MOVEMENT],
                3: [classFeature.DEFLECT_MISSILES, classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI, classFeature.SLOW_FALL],
                5: [classFeature.EXTRA_ATTACK, classFeature.STUNNING_STRIKE], #? Is this the same Extra Attack as Barbarian?
                6: [classFeature.KI_STRIKES, classFeature.SUBCLASS_FEATURE],
                7: [classFeature.EVASION, classFeature.STILLNESS_OF_MIND],
                8: [classFeature.ASI],
                9: [classFeature.UNARMORED_MOVEMENT],
                10: [classFeature.PURITY_OF_BODY],
                11: [classFeature.SUBCLASS_FEATURE],
                12: [classFeature.ASI],
                13: [classFeature.TONGUE_OF_THE_SUN_AND_MOON],
                14: [classFeature.DIAMOND_SOUL],
                15: [classFeature.TIMELESS_BODY],
                16: [classFeature.ASI],
                17: [classFeature.SUBCLASS_FEATURE],
                18: [classFeature.EMPTY_BODY],
                19: [classFeature.ASI],
                20: [classFeature.PERFECT_SELF]
            }
            #? And what about Martial Arts die? and Ki Points? etc. Map later.
        )

@registered
@sourcebook(Sourcebooks.PHB14)
class Paladin(Class):
    def __init__(self):
        super().__init__(
            name="Paladin",
            hitDie=10,
            savingThrowProf=[
                AbilityScore.WISDOM,
                AbilityScore.CHARISMA
            ],
            skillProf={
                2: [
                    Skill.ATHLETICS,
                    Skill.INSIGHT,
                    Skill.INTIMIDATION,
                    Skill.MEDICINE,
                    Skill.PERSUASION,
                    Skill.RELIGION
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                WeaponCategory.MARTIAL
            ],
            toolProf=[],
            armorProf=[
                ArmorCategory.LIGHT,
                ArmorCategory.MEDIUM,
                ArmorCategory.HEAVY,
                ArmorCategory.SHIELDS
            ],
            startingEquipment=PaladinSet,
            levelFeatures={
                1: [classFeature.DIVINE_SENSE, classFeature.LAY_ON_HANDS],
                2: [classFeature.DIVINE_SMITE, classFeature.FIGHTING_STYLE, classFeature.SPELLCASTING],
                3: [classFeature.DIVINE_HEALTH, classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI],
                5: [classFeature.EXTRA_ATTACK],
                6: [classFeature.AURA_OF_PROTECTION],
                7: [classFeature.SUBCLASS_FEATURE],
                8: [classFeature.ASI],
                9: [],
                10: [classFeature.AURA_OF_COURAGE],
                11: [classFeature.DIVINE_SMITE],
                12: [classFeature.ASI],
                13: [],
                14: [classFeature.CLEANSING_TOUCH],
                15: [classFeature.SUBCLASS_FEATURE],
                16: [classFeature.ASI],
                17: [],
                18: [classFeature.AURA_IMPROVEMENTS],
                19: [classFeature.ASI],
                20: [classFeature.SUBCLASS_FEATURE]
            },
            spellSlotTree=HalfCastTree
        )
        
@registered
@sourcebook(Sourcebooks.PHB14)
class Ranger(Class):
    def __init__(self):
        super().__init__(
            name="Ranger",
            hitDie=10,
            savingThrowProf=[
                AbilityScore.STRENGTH,
                AbilityScore.DEXTERITY
            ],
            skillProf={
                3: [
                    Skill.ANIMAL_HANDLING,
                    Skill.ATHLETICS,
                    Skill.INSIGHT,
                    Skill.INVESTIGATION,
                    Skill.NATURE,
                    Skill.PERCEPTION,
                    Skill.STEALTH,
                    Skill.SURVIVAL
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                WeaponCategory.MARTIAL
            ],
            toolProf=[],
            armorProf=[
                ArmorCategory.LIGHT,
                ArmorCategory.MEDIUM,
                ArmorCategory.SHIELDS
            ],
            startingEquipment=RangerSet,
            levelFeatures={
                1: [classFeature.FAVORED_ENEMY, classFeature.NATURAL_EXPLORER],
                2: [classFeature.FIGHTING_STYLE, classFeature.SPELLCASTING],
                3: [classFeature.SUBCLASS_CHOICE, classFeature.PRIMEVAL_AWARENESS],
                4: [classFeature.ASI],
                5: [classFeature.EXTRA_ATTACK],
                6: [classFeature.FAVORED_ENEMY, classFeature.NATURAL_EXPLORER],
                7: [classFeature.SUBCLASS_FEATURE],
                8: [classFeature.ASI, classFeature.LANDS_STRIDE],
                9: [],
                10: [classFeature.HIDE_IN_PLAIN_SIGHT, classFeature.NATURAL_EXPLORER],
                11: [classFeature.SUBCLASS_FEATURE],
                12: [classFeature.ASI],
                13: [],
                14: [classFeature.VANISH, classFeature.FAVORED_ENEMY],
                15: [classFeature.SUBCLASS_FEATURE],
                16: [classFeature.ASI],
                17: [],
                18: [classFeature.FERAL_SENSES],
                19: [classFeature.ASI],
                20: [classFeature.FOE_SLAYER]
            },
            spellSlotTree=HalfCastTree,
            spellsKnownAtLevel={
                 1: 0,
                 2: 2,
                 3: 3,
                 4: 3,
                 5: 4,
                 6: 4,
                 7: 5,
                 8: 5,
                 9: 6,
                10: 6,
                11: 7,
                12: 7,
                13: 8,
                14: 8,
                15: 9,
                16: 9,
                17: 10,
                18: 10,
                19: 11,
                20: 11
            }
        )


@registered
@sourcebook(Sourcebooks.PHB14)
class Rogue(Class):
    def __init__(self):
        super().__init__(
            name="Rogue",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.DEXTERITY,
                AbilityScore.INTELLIGENCE
            ],
            skillProf={
                4: [
                    Skill.ACROBATICS,
                    Skill.ATHLETICS,
                    Skill.DECEPTION,
                    Skill.INSIGHT,
                    Skill.INTIMIDATION,
                    Skill.INTIMIDATION,
                    Skill.PERCEPTION,
                    Skill.PERFORMANCE,
                    Skill.PERSUASION,
                    Skill.SLEIGHT_OF_HAND,
                    Skill.STEALTH
                ]
            },
            weaponProf=[
                WeaponCategory.SIMPLE,
                Weapons.CROSSBOWS_HAND,
                Weapons.LONGSWORDS,
                Weapons.RAPIERS,
                Weapons.SHORTSWORDS
            ],
            toolProf=[Tools.THIEVES_TOOLS],
            armorProf=[ArmorCategory.LIGHT],
            startingEquipment=RogueSet,
            levelFeatures={
                1: [classFeature.EXPERTISE, classFeature.SNEAK_ATTACK, classFeature.THEIVES_CANT],
                2: [classFeature.CUNNING_ACTION],
                3: [classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI],
                5: [classFeature.UNCANNY_DODGE],
                6: [classFeature.EXPERTISE],
                7: [classFeature.EVASION],
                8: [classFeature.ASI],
                9: [classFeature.SUBCLASS_FEATURE],
                10: [classFeature.ASI],
                11: [classFeature.RELIABLE_TALENT],
                12: [classFeature.ASI],
                13: [classFeature.SUBCLASS_FEATURE],
                14: [classFeature.BLINDSENSE],
                15: [classFeature.SLIPPERY_MIND],
                16: [classFeature.ASI],
                17: [classFeature.SUBCLASS_FEATURE],
                18: [classFeature.ELUSIVE],
                19: [classFeature.ASI],
                20: [classFeature.STROKE_OF_LUCK]
            }
        )

@registered
@sourcebook(Sourcebooks.PHB14)
class Sorcerer(Class):
    def __init__(self):
        super().__init__(
            name="Sorcerer",
            hitDie=6,
            savingThrowProf=[
                AbilityScore.CONSTITUTION,
                AbilityScore.CHARISMA
            ],
            skillProf={
                2: [
                    Skill.ARCANA,
                    Skill.DECEPTION,
                    Skill.INSIGHT,
                    Skill.INTIMIDATION,
                    Skill.PERSUASION,
                    Skill.RELIGION
                ]
            },
            weaponProf=[
                Weapons.DAGGERS,
                Weapons.DARTS,
                Weapons.SLINGS,
                Weapons.QUARTERSTAVES,
                Weapons.CROSSBOWS_LIGHT
            ],
            toolProf=[],
            armorProf=[],
            startingEquipment=SorcererSet,
            levelFeatures={
                1: [classFeature.SPELLCASTING, classFeature.SUBCLASS_CHOICE],
                2: [classFeature.FONT_OF_MAGIC],
                3: [classFeature.METAMAGIC],
                4: [classFeature.ASI],
                5: [],
                6: [classFeature.SUBCLASS_FEATURE],
                7: [],
                8: [classFeature.ASI],
                9: [],
                10: [classFeature.METAMAGIC],
                11: [],
                12: [classFeature.ASI],
                13: [],
                14: [classFeature.SUBCLASS_FEATURE],
                15: [],
                16: [classFeature.ASI],
                17: [classFeature.METAMAGIC],
                18: [classFeature.SUBCLASS_FEATURE],
                19: [classFeature.ASI],
                20: [classFeature.CLASS_CAPSTONE]
            },
            spellSlotTree=FullCastTree,
            cantripsKnownAtLevel={
                1: 4,
                2: 4,
                3: 4,
                4: 5,
                5: 5,
                6: 5,
                7: 5,
                8: 5,
                9: 5,
                10: 6,
                11: 6,
                12: 6,
                13: 6,
                14: 6,
                15: 6,
                16: 6,
                17: 6,
                18: 6,
                19: 6,
                20: 6 
            },
            spellsKnownAtLevel={
                1: 2,
                2: 3,
                3: 4,
                4: 5,
                5: 6,
                6: 7,
                7: 8,
                8: 9,
                9: 10,
                10: 11,
                11: 12,
                12: 12,
                13: 13,
                14: 13,
                15: 14,
                16: 14,
                17: 15,
                18: 15,
                19: 15,
                20: 15
            }
        )
        

@registered
@sourcebook(Sourcebooks.PHB14)
class Warlock(Class):
    def __init__(self):
        super().__init__(
            name="Warlock",
            hitDie=8,
            savingThrowProf=[
                AbilityScore.WISDOM,
                AbilityScore.CHARISMA
            ],
            skillProf={
                2: [
                    Skill.ARCANA,
                    Skill.DECEPTION,
                    Skill.HISTORY,
                    Skill.INTIMIDATION,
                    Skill.INVESTIGATION,
                    Skill.NATURE,
                    Skill.RELIGION
                ]
            },
            weaponProf=[WeaponCategory.SIMPLE],
            toolProf=[],
            armorProf=[ArmorCategory.LIGHT],
            startingEquipment=WarlockSet,
            levelFeatures={
                1: [classFeature.PACT_MAGIC, classFeature.SUBCLASS_CHOICE],
                2: [classFeature.ELDRDRITCH_INVOCATIONS],
                3: [classFeature.PACT_BOON],
                4: [classFeature.ASI],
                5: [],
                6: [classFeature.SUBCLASS_FEATURE],
                7: [],
                8: [classFeature.ASI],
                9: [],
                10: [classFeature.SUBCLASS_FEATURE],
                11: [classFeature.MYSTIC_ARCANUM],
                12: [classFeature.ASI],
                13: [classFeature.MYSTIC_ARCANUM],
                14: [classFeature.SUBCLASS_FEATURE],
                15: [classFeature.MYSTIC_ARCANUM],
                16: [classFeature.ASI],
                17: [classFeature.MYSTIC_ARCANUM],
                18: [],
                19: [classFeature.ASI],
                20: [classFeature.CLASS_CAPSTONE]
            },
            spellSlotTree=PactCastTree,
            cantripsKnownAtLevel={
                1: 2,
                2: 2,
                3: 2,
                4: 3,
                5: 3,
                6: 3,
                7: 3,
                8: 3,
                9: 3,
                10: 4,
                11: 4,
                12: 4,
                13: 4,
                14: 4,
                15: 4,
                16: 4,
                17: 4,
                18: 4,
                19: 4,
                20: 4 
            },
            spellsKnownAtLevel={
                1: 2,
                2: 3,
                3: 4,
                4: 5,
                5: 6,
                6: 7,
                7: 8,
                8: 9,
                9: 10,
                10: 10,
                11: 11,
                12: 11,
                13: 12,
                14: 12,
                15: 13,
                16: 13,
                17: 14,
                18: 14,
                19: 15,
                20: 15
            }
        )

@registered
@sourcebook(Sourcebooks.PHB14)
class Wizard(Class):
    def __init__(self):
        super().__init__(
            name="Wizard",
            hitDie=6,
            savingThrowProf=[
                AbilityScore.INTELLIGENCE, 
                AbilityScore.WISDOM
            ],
            skillProf={
                2: [
                    Skill.ARCANA, 
                    Skill.HISTORY, 
                    Skill.INSIGHT, 
                    Skill.INVESTIGATION, 
                    Skill.MEDICINE, 
                    Skill.RELIGION
                ]
            },
            toolProf=[],
            weaponProf=[
                Weapons.DAGGERS,
                Weapons.DARTS,
                Weapons.SLINGS,
                Weapons.QUARTERSTAVES,
                Weapons.CROSSBOWS_LIGHT
            ],
            armorProf=[],
            startingEquipment=WizardSet,
            levelFeatures={
                1: [classFeature.SPELLCASTING, classFeature.ARCANE_RECOVERY],
                2: [classFeature.SUBCLASS_CHOICE],
                4: [classFeature.ASI],
                6: [classFeature.SUBCLASS_FEATURE],
                8: [classFeature.ASI],
                10: [classFeature.SUBCLASS_FEATURE],
                12: [classFeature.ASI],
                14: [classFeature.SUBCLASS_FEATURE],
                16: [classFeature.ASI],
                18: [classFeature.SPELL_MASTERY],
                19: [classFeature.ASI],
                20: [classFeature.SIGNATURE_SPELLS]
            },
            spellSlotTree=FullCastTree,
            cantripsKnownAtLevel={
                1: 3,
                2: 3,
                3: 3,
                4: 4,
                5: 4,
                6: 4,
                7: 4,
                8: 4,
                9: 4,
                10: 5,
                11: 5,
                12: 5,
                13: 5,
                14: 5,
                15: 5,
                16: 5,
                17: 5,
                18: 5,
                19: 5,
                20: 5 
            }
        )