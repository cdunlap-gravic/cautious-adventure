
#@ This module is here just for the sake of readability of <rulebook>_Class.py. Nothing else. - Jeahnoh
#! Actually, not anymore. Need to utilize this for Background equipments too, and can utilize for lootsets
BarbarianSet={}
BardSet={}
ClericSet={}
DruidSet={}
FighterSet={
          # I SHOULD CHECK IF THIS IS A STANDARD ARRAY OF OPTIONS, OR EVEN JUST ABSTRACT THIS TO a "FIGHTER'S SET OR GOLD" for ease of reading.
    1: [    # START WITH EQUIPMENT
            { 
                1: [
                    "Chain Mail",
                    [
                        "Leather Armor",
                        "Long Bow",
                        "20 Arrows"
                    ]
                ],
                1: [
                    [
                        "Martial Weapon",
                        "Shield"
                    ],
                    [
                        "Martial Weapon",
                        "Martial Weapon"
                    ] 
                ],
                1: [
                    [
                        "Light Crossbow",
                        "20 Bolts"
                    ],
                    [
                        "Handaxe",
                        "Handaxe"
                    ]
                ],
                1: [
                    "Dungeoneer's Pack",
                    "Explorer's Pack"
                ]
            }, # OR START WITH GOLD
        "5d4 * 10 gold"
    ]   
            
}
MonkSet={}
PaladinSet={}
RangerSet={}
RogueSet={}
SorcererSet={}
WarlockSet={}
WizardSet={      # I SHOULD CHECK IF THIS IS A STANDARD ARRAY OF OPTIONS, OR EVEN JUST ABSTRACT THIS TO a "FIGHTER'S SET OR GOLD" for ease of reading.
    1: [    # START WITH EQUIPMENT
            [
                { 
                    1: [
                        "Quarterstaff",
                        "Dagger"
                    ],
                    1: [
                        "Component Pouch",
                        "Arcane Focus" #@ Definitely a category tag
                    ],
                    1: [
                        "Scholar's Pack",
                        "Explorer's Pack"
                    ]
                },
            "Spellbook"
            ], # OR START WITH GOLD
        "4d4 * 10 gold"
    ]   
}