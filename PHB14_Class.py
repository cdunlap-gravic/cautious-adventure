from newClass import Class, registered, sourcebook

@registered
@sourcebook("PHB'14")
class Fighter(Class):
    def __init__(self):
        super().__init__(
            name="Fighter",
            hitDice="d10",
            savingThrowProf=[
                "STR", 
                "CON"
            ],
            skillProf={
                1: (2, [
                    "Athletics", 
                    "Acrobatics", 
                    "Animal Handling", 
                    "History", 
                    "Insight", 
                    "Intimidation", 
                    "Perception", 
                    "Survival"
                    ]),
                2: [
                    "Athletics", 
                    "Acrobatics", 
                    "Animal Handling", 
                    "History", 
                    "Insight", 
                    "Intimidation", 
                    "Perception", 
                    "Survival"
                ]
            },
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
class Wizard(Class):
    def __init__(self):
        super().__init__(
            name="Wizard",
            hitDice="d6",
            savingThrowProf=[
                "INT", 
                "WIS"
            ],
            skillProf={
                1: (2, [
                    "Arcana", 
                    "History", 
                    "Insight", 
                    "Investigation", 
                    "Medicine", 
                    "Religion"]),
                2: [
                    "Arcana", 
                    "History", 
                    "Insight", 
                    "Investigation", 
                    "Medicine", 
                    "Religion"
                ]
            },
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
            }
        )