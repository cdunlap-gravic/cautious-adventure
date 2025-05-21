# STANDARD IMPORTS FOR CLASS SETS
from core.types import AbilityScore, Skill

from core.Class import Class, registered, sourcebook
from core.SpellSlotTree import FullCastTree, HalfCastTree, PactCastTree

# RULEBOOK SPECIFIC IMPORTS
from PHB14_EquipmentSets import *


#? So how do we want to handle extras like rage count, or rage damage? Extra table?
#? And how do we handle multiclass requirements? Lets at least populate out the rest first...
@registered
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Martial Weapons"
            ],
            toolProf=[],
            armorProf=[
                "Light Armor",
                "Medium Armor",
                "Shields"
            ],
            startingEquipment=BarbarianSet,
            levelFeatures={
                1: ["Rage", "Unarmored Defense"],
                2: ["Danger Sense", "Reckless Attack"],
                3: ["Primal Path"],
                4: ["ASI or Feat"],
                5: ["Extra Attack", "Fast Movement"],
                6: ["Path Feature"],
                7: ["Feral Instinct"],
                8: ["ASI or Feat"],
                9: ["Brutal Critical"],
                10: ["Path Feature"],
                11: ["Relentless Rage"],
                12: ["ASI or Feat"],
                13: ["Brutal Critical"],
                14: ["Path Feature"],
                15: ["Persistent Rage"],
                16: ["ASI or Feat"],
                17: ["Brutal Critical"],
                18: ["Indomitable Might"],
                19: ["ASI or Feat"],
                20: ["Primal Champion"]
            }
        )
@registered
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Hand Crossbows",
                "Longswords",
                "Rapiers",
                "Shortswords"
            ],
            toolProf=["3 Musical Instruments"], # We'll just figure this one out later...
            armorProf=[
                "Light Armor"
            ],
            startingEquipment=None,
            levelFeatures={
                1: ["Bardic Inspiration", "Spellcasting"],
                2: ["Jack of All Trades", "Song of Rest"],
                3: ["Bard College", "Expertise"],
                4: ["ASI or Feat"],
                5: ["Bardic Inspiration", "Font of Inspiration"],
                6: ["Countercharm", "Bard College feature"],
                7: [],
                8: ["ASI or Feat"],
                9: ["Song of Rest"],
                10: ["Bardic Inspiration", "Expertise", "Magical Secrets"],
                11: [],
                12: ["ASI or Feat"],
                13: ["Song of Rest"],
                14: ["Magical Secrets", "Bard College feature"],
                15: ["Bardic Inspiration"],
                16: ["ASI or Feat"],
                17: ["Song of Rest"],
                18: ["Magical Secrets"],
                19: ["ASI or Feat"],
                20: ["Superior Inspiration"]
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
@sourcebook("PHB'14")
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
                "Simple Weapons"
            ],
            toolProf=[],
            armorProf=[
                "Light Armor",
                "Medium Armor",
                "Shields"
            ],
            startingEquipment=ClericSet,
            levelFeatures={
                1: ["Spellcasting", "Divine Domain"],
                2: ["Channel Divinity", "Divine Domaine Feature"],
                3: [],
                4: ["ASI or Feat"],
                5: ["Destroy Undead"],
                6: ["Channel Divinity", "Divine Domain Feature"],
                7: [],
                8: ["ASI or Feat", "Destroy Undead", "Divine Domain Feature"],
                9: [],
                10: ["Divine Intervention"],
                11: ["Destroy Undead"],
                12: ["ASI or Feat"],
                13: [],
                14: ["Destroy Undead"],
                15: [],
                16: ["ASI or Feat"],
                17: ["Destroy Undead", "Divine Domain Feature"],
                18: ["Channel Divinity"],
                19: ["ASI or Feat"],
                20: ["Divine Intervention"]
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
@sourcebook("PHB'14")
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
                "Clubs",
                "Daggers", 
                "Darts",
                "Javelins",
                "Maces",
                "Quarterstaves",
                "Scimitars",
                "Sickles",
                "Slings",
                "Spears"
            ],
            toolProf=["Herbalism Kit"],
            armorProf=[
                "Light Armor",
                "Medium Armor",
                "Shields",
                "Exclude Metal" # Yeah no fuck that rule. This is stupid.
            ],
            startingEquipment=DruidSet,
            levelFeatures={
                1: ["Druidic", "Spellcasting"],
                2: ["Wild Shape", "Druid Circle"],
                3: [],
                4: ["Wild Shape Improvement", "ASI or Feat"],
                5: [],
                6: ["Druid Circle Feature"],
                7: [],
                8: ["Wild Shape Improvement", "ASI or Feat"],
                9: [],
                10: ["Druid Circle Feature"],
                11: [],
                12: ["ASI or Feat"],
                13: [],
                14: ["Druid Circle Feature"],
                15: [],
                16: ["ASI or Feat"],
                17: [],
                18: ["Timeless Body", "Beast Spells"],
                19: ["ASI or Feat"],
                20: ["Archdruid"]
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
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Martial Weapons"
            ],
            toolProf=[],
            armorProf=[
                "Light Armor", # this line should look more like Equipment.Armours.tag["light"] These tags will only be a placeholder for now.
                "Medium Armor",
                "Heavy Armor",
                "Shields"
            ],
            startingEquipment=FighterSet,
            levelFeatures={
                1: ["Fighting Style", "Second Wind"],
                2: ["Action Surge"],
                3: ["Martial Archetype"],
                4: ["ASI or Feat", "Martial Versatility (Optional)"],
                5: ["Extra Attack"],
                6: ["ASI or Feat", "Martial Versatility (Optional)"],
                7: ["Martial Archetype Feature"],
                8: ["ASI or Feat", "Martial Versatility (Optional)"],
                9: ["Indomitable"],
                10: ["Martial Archetype Feature"],
                11: ["Extra Attack"],
                12: ["ASI or Feat", "Martial Versatility (Optional)"],
                13: ["Indomitable"],
                14: ["ASI or Feat", "Martial Versatility (Optional)"],
                15: ["Martial Archetype Feature"],
                16: ["ASI or Feat", "Martial Versatility (Optional)"],
                17: ["Action Surge", "Indomitable"],
                18: ["Martial Archetype Feature"],
                19: ["ASI or Feat", "Martial Versatility (Optional)"],
                20: ["Extra Attack"]
            }
        )


@registered
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Shortswords"
            ],
            toolProf={
                1: [
                    "Artisan's Tools",
                    "Musical Instrument"
                ]
            },
            armorProf=[],
            startingEquipment=MonkSet,
            levelFeatures={
                1: ["Unarmored Defence", "Martial Arts"],
                2: ["Ki", "Unarmored Movement"],
                3: ["Deflect Missiles", "Monastic Tradition"],
                4: ["ASI or Feat", "Slow Fall"],
                5: ["Extra Attack", "Stunning Strike"], #? Is this the same Extra Attack as Barbarian?
                6: ["Ki-Empowered Strikes", "Monastic Tradition Feature"],
                7: ["Evasion", "Stillness of Mind"],
                8: ["ASI or Feat"],
                9: ["Unarmored Movement Improvement"],
                10: ["Purity of Body"],
                11: ["Monastic Tradition Feature"],
                12: ["ASI or Feat"],
                13: ["Tongue of the Sun and Moon"],
                14: ["Diamond Soul"],
                15: ["Timeless Body"],
                16: ["ASI or Feat"],
                17: ["Monastic Tradition Feature"],
                18: ["Empty Body"],
                19: ["ASI or Feat"],
                20: ["Perfect Self"]
            }
            #? And what about Martial Arts die? and Ki Points? etc. Map later.
        )

@registered
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Martial Weapons"
            ],
            toolProf=[],
            armorProf=[
                "Light Armor",
                "Medium Armor",
                "Heavy Armor",
                "Shields"
            ],
            startingEquipment=PaladinSet,
            levelFeatures={
                1: ["Divine Sense", "Lay on Hands"],
                2: ["Divine Smite", "Fighting Style", "Spellcasting"],
                3: ["Divine Health", "Sacred Oath"],
                4: ["ASI or Feat"],
                5: ["Extra Attack"],
                6: ["Aura of Protection"],
                7: ["Sacred Oath Feature"],
                8: ["ASI or Feat"],
                9: [],
                10: ["Aura of Courage"],
                11: ["Improved Divine Smite"],
                12: ["ASI or Feat"],
                13: [],
                14: ["Cleansing Touch"],
                15: ["Sacred Oath Feature"],
                16: ["ASI or Feat"],
                17: [],
                18: ["Aura Improvements"],
                19: ["ASI or Feat"],
                20: ["Sacred Oath Feature"]
            },
            spellSlotTree=HalfCastTree
        )
        
@registered
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Martial Weapons"
            ],
            toolProf=[],
            armorProf=[
                "Light Armor",
                "Medium Armor",
                "Shields"
            ],
            startingEquipment=RangerSet,
            levelFeatures={
                1: ["Favored Enemy", "Natural Explorer"],
                2: ["Fighting Style", "Spellcasting"],
                3: ["Ranger Archetype", "Primeval Awareness"],
                4: ["ASI or Feat"],
                5: ["Extra Attack"],
                6: ["Favored Enemy Improvements", "Natural Explorer Improvements"],
                7: ["Ranger Archetype Feature"],
                8: ["ASI or Feat", "Land's Stride"],
                9: [],
                10: ["Hide in Plain Sight", "Natural Explorer Improvement"],
                11: ["Ranger Archetype Feature"],
                12: ["ASI or Feat"],
                13: [],
                14: ["Vanish", "Favored Enemy Improvement"],
                15: ["Ranger Archetype Feature"],
                16: ["ASI or Feat"],
                17: [],
                18: ["Feral Senses"],
                19: ["ASI or Feat"],
                20: ["Foe Slayer"]
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
@sourcebook("PHB'14")
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
                "Simple Weapons",
                "Hand Crossbows",
                "Longswords",
                "Rapiers",
                "Shortswords"
            ],
            toolProf=["Thieve's Tools"],
            armorProf=["Light Armor"],
            startingEquipment=RogueSet,
            levelFeatures={
                1: ["Expertise", "Sneak Attack", "Thieves' Cant"],
                2: ["Cunning Action"],
                3: ["Roguish Archetype"],
                4: ["ASI or Feat"],
                5: ["Uncanny Dodge"],
                6: ["Expertise"],
                7: ["Evasion"],
                8: ["ASI or Feat"],
                9: ["Roguish Archetype Feature"],
                10: ["ASI or Feat"],
                11: ["Reliable Talent"],
                12: ["ASI or Feat"],
                13: ["Roguish Archetype Feature"],
                14: ["Blindsense"],
                15: ["Slippery Mind"],
                16: ["ASI or Feat"],
                17: ["Roguish Archetype Feature"],
                18: ["Elusive"],
                19: ["ASI or Feat"],
                20: ["Stroke of Luck"]
            }
        )

@registered
@sourcebook("PHB'14")
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
                "Daggers",
                "Darts",
                "Slings",
                "Quarterstaves",
                "Light Crossbowws"
            ],
            toolProf=[],
            armorProf=[],
            startingEquipment=SorcererSet,
            levelFeatures={
                1: ["Spellcasting", "Sorcerous Origin"],
                2: ["Font of Magic"],
                3: ["Metamagic"],
                4: ["ASI or Feat"],
                5: [],
                6: ["Sorcerous Origin Feature"],
                7: [],
                8: ["ASI or Feat"],
                9: [],
                10: ["Metamagic"],
                11: [],
                12: ["ASI or Feat"],
                13: [],
                14: ["Sorcerous Origin Feature"],
                15: [],
                16: ["ASI or Feat"],
                17: ["Metamagic"],
                18: ["Sorcerous Origin Feature"],
                19: ["ASI or Feat"],
                20: ["Sorcerous Restoration"]
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
@sourcebook("PHB'14")
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
            weaponProf=["Simple Weapons"],
            toolProf=[],
            armorProf=["Light Armor"],
            startingEquipment=WarlockSet,
            levelFeatures={
                1: ["Pact Magic", "Otherworldly Patron"],
                2: ["Eldritch Invocations"],
                3: ["Pact Boon"],
                4: ["ASI or Feat"],
                5: [],
                6: ["Otherworldly Patron Feature"],
                7: [],
                8: ["ASI or Feat"],
                9: [],
                10: ["Otherworldly Patron Feature"],
                11: ["Mystic Arcanum"],
                12: ["ASI or Feat"],
                13: ["Mystic Arcanum"],
                14: ["Otherworldly Patron Feature"],
                15: ["Mystic Arcanum"],
                16: ["ASI or Feat"],
                17: ["Mystic Arcanum"],
                18: [],
                19: ["ASI or Feat"],
                20: ["Eldritch Master"]
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
@sourcebook("PHB'14")
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
                "Daggers",
                "Darts",
                "Slings",
                "Quarterstaves",
                "Light Crossbows"
            ],
            armorProf=[],
            startingEquipment=WizardSet,
            levelFeatures={
                1: ["Spellcasting", "Arcane Recovery"],
                2: ["Arcane Tradition"],
                3: ["Cantrip Formulas (Optional)"],
                4: ["ASI or Feat"],
                6: ["Arcane Tradition feature"],
                8: ["ASI or Feat"],
                10: ["Arcane Tradition feature"],
                12: ["ASI or Feat"],
                14: ["Arcane Tradition feature"],
                16: ["ASI or Feat"],
                18: ["Spell Mastery"],
                19: ["ASI or Feat"],
                20: ["Signature Spells"]
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