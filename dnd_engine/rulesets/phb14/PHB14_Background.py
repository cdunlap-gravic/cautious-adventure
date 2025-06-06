# STANDARD IMPORTS FOR CLASS SETS
from core.Background import Background, registered, sourcebook
from core.types import Skill, Sourcebooks, Tools
from PHB14_Feats import *

#@
#@ are features feats? or are they of the same ilk as class features?
#@


#Acolyte
@registered
@sourcebook(Sourcebooks.PHB14)
class Acolyte(Background):
    def __init__(self):
        super().__init__(
            name="Acolyte",
            skillProf=[
                Skill.INSIGHT,
                Skill.RELIGION
            ],
            toolProf=[],
            languages=["Pick 2 Languages"],
            equipment=[
                "Holy Symbol",
                "Prayer Book/Wheel",
                "5 Incense",
                "vestments",
                "common clothes",
                "belt pouch",
                "15 gold"
            ],
            features=["Shelter of the Faithful"]
        )


#Charlatan
@registered
@sourcebook(Sourcebooks.PHB14)
class Charlatan(Background):
    def __init__(self):
        super().__init__(
            name="Charlatan",
            skillProf=[
                Skill.DECEPTION,
                Skill.SLEIGHT_OF_HAND
            ],
            toolProf=[
                Tools.DISGUISE_KIT,
                Tools.FORGERY_KIT
            ],
            languages=[],
            equipment=[
                "Fine Clothes",
                "Disguise Kit",
                "Con Items (weighted dice etc)",
                "Belt Pouch",
                "15 gold"
            ],
            features=["False Identity"]
        )

#Criminal
@registered
@sourcebook(Sourcebooks.PHB14)
class Criminal(Background):
    def __init__(self):
        super().__init__(
            name="Criminal",
            skillProf=[
                Skill.DECEPTION,
                Skill.STEALTH
            ],
            toolProf=[
                "Gaming set (five types)",
                Tools.THIEVES_TOOLS
            ],
            languages=[],
            equipment=[
                "Crowbar",
                "dark common clothes",
                "hood",
                "belt pouch",
                "15 gold"
            ],
            features=["Criminal Contact"]
        )
        
        
#Criminal (Spy)
@registered
@sourcebook(Sourcebooks.PHB14)
class Criminal_Spy(Criminal):
    def __init__(self):
        super().__init__()
        self.name="Criminal (Spy)"
        self.features=["Spy Contact"]
        
        
#Custom Background
#! This one is very special and will probably be more difficult to configure until the whole system is finalized
#@registered
@sourcebook(Sourcebooks.PHB14)
class Custom(Background):
    def __init__(self):
        super().__init__(
            name="<CUSTOM>",
            skillProf=[
                "Any 2"
            ],
            toolProf=[
                "Any 2 or languages"
            ],
            languages=[
                "any 2 or tool prof"
            ],
            equipment=[
                "preexisitng background equip pack" #which means I should abstract this out to equipment sets
            ],
            features=[
                "CUSTOM BACKGROUND",
                "ur gonna do a mad libs"
            ]
        )
        
        
#Entertainer
@registered
@sourcebook(Sourcebooks.PHB14)
class Entertainer(Background):
    def __init__(self):
        super().__init__(
            name="Entertainer",
            skillProf=[
                Skill.ACROBATICS,
                Skill.PERFORMANCE
            ],
            toolProf=[
                Tools.DISGUISE_KIT,
                Tools.MUSICAL_INSTRUMENT
            ],
            languages=[],
            equipment=[
                Tools.MUSICAL_INSTRUMENT,
                "favor of an admirer",
                "costume clothes",
                "belt pouch",
                "15 gold"
            ],
            features=["By Popular Demand"]
            #? Maybe incorporate specialties here for when I make this character sheet system an actual runable game?
        )
        
        
#Entertainer (Gladiator)
@registered
@sourcebook(Sourcebooks.PHB14)
class Entertainer_Gladiator(Entertainer):
    def __init__(self):
        super().__init__()
        self.name="Entertainer (Gladiator)",
        self.equipment.remove(Tools.MUSICAL_INSTRUMENT)
        self.equipment.append("Choose 1 Unusual Weapon")
        
        
#Folk Hero
@registered
@sourcebook(Sourcebooks.PHB14)
class FolkHero(Background):
    def __init__(self):
        super().__init__(
            name="Folk Hero",
            skillProf=[
                Skill.ANIMAL_HANDLING,
                Skill.SURVIVAL
            ],
            toolProf=[
                Tools.ARTISANS_TOOLS,
                "vehicles (land)"
            ],
            languages=[],
            equipment=[
                Tools.ARTISANS_TOOLS,
                "Shovel",
                "Iron Pot",
                "Common Clothes",
                "belt pouch",
                "10 gold"
            ],
            features=["Rustic Hospitality"]
        )
        
        
#Guild Artisan
@registered
@sourcebook(Sourcebooks.PHB14)
class GuildArtisan(Background):
    def __init__(self):
        super().__init__(
            name="Guild Artisan",
            skillProf=[
                Skill.INSIGHT,
                Skill.PERSUASION
            ],
            toolProf=[Tools.ARTISANS_TOOLS],
            languages=["choose 1"],
            equipment=[
                "Choose 1 Artisan's Tools",
                "letter of introduction",
                "traveler's clothes",
                "belt pouch",
                "15 gold"
            ],
            features=["Guild Membership"]
        )
        
        
#Guild Artisan (Guild Merchant)
@registered
@sourcebook(Sourcebooks.PHB14)
class GuildArtisan_Merchant(GuildArtisan):
    def __init__(self):
        super().__init__()
        self.name="Guild Artisan (Guild Merchant)"
        self.toolProf.remove("Choose 1 Artisan's Tools")
        self.toolProf.append({1: ["Choose 1 Artisan's Tools", "Navigator's Tools"]})
        self.languages.append("Choose 1 additonal language or the tools") #! This will be special to add in
        self.equipment.remove("Choose 1 Artisan's Tools")
        self.equipment.append({1: ["Choose 1 Artisan's Tools", "Mule and Cart"]})
        
        
#Hermit
@registered
@sourcebook(Sourcebooks.PHB14)
class Hermit(Background):
    def __init__(self):
        super().__init__(
            name="Hermit",
            skillProf=[
                Skill.MEDICINE,
                Skill.RELIGION
            ],
            toolProf=[Tools.HERBALISM_KIT],
            languages=["Choose 1 Language"],
            equipment=[
                "Scroll Case",
                "Winter Blanket",
                "Common Clothes",
                "Herbalism Kit",
                "5 gold"
            ],
            features=["Discovery"]
        )
        
#Noble
@registered      
@sourcebook(Sourcebooks.PHB14)
class Noble(Background):
    def __init__(self):
        super().__init__(
            name="Noble",
            skillProf=[
                Skill.HISTORY,
                Skill.PERSUASION
            ],
            toolProf=["Gaming set (one type)"],
            languages=["Choose 1 Language"],
            equipment=[
                "Fine Clothes",
                "Signet Ring",
                "Scroll of Pedigree",
                "Purse",
                "25 gold"
            ],
            features=["Position of Priviledge"]
        )

        
#Noble (Knight)
@registered
@sourcebook(Sourcebooks.PHB14)
class Noble_Knight(Noble):
    def __init__(self):
        super().__init__()
        self.name="Noble (Knight)"
        self.features.remove("Position of Priviledge")
        self.features.append({1: ["Position of Priviledge","Retainers"]})         
        
        
        
#Noble (Retainers)
@registered
@sourcebook(Sourcebooks.PHB14)
class Noble_Retainers(Noble):
    def __init__(self):
        super().__init__()
        self.name="Noble (Retainers)"
        self.features.remove("Position of Priviledge")
        self.features.append("Retainers")   

        
#Outlander
@registered
@sourcebook(Sourcebooks.PHB14)
class Outlander(Background):
    def __init__(self):
        super().__init__(
            name="Outlander",
            skillProf=[
                Skill.ATHLETICS,
                Skill.SURVIVAL
            ],
            toolProf=[Tools.MUSICAL_INSTRUMENT],
            languages=["Choose 1 Language"],
            equipment=[
                "Staff",
                "Hunting Trap",
                "Animal Trophy",
                "Traveler's Clothes",
                "pouch",
                "10 gold"
            ],
            features=["Wanderer"]
        )
        
        
#Sage
@registered
@sourcebook(Sourcebooks.PHB14)
class Sage(Background):
    def __init__(self):
        super().__init__(
            name="Sage",
            skillProf=[
                Skill.ARCANA,
                Skill.HISTORY
            ],
            toolProf=[],
            languages=["Choose 2 Languages"],
            equipment=[
                "Bottle of Black Ink",
                "Quill",
                "Small Knife",
                "Deceased Question Letter",
                "Common Clothes",
                "pouch",
                "10 Gold"
            ],
            features=["Researcher"]
        )
        
        
#Sailor
@registered
@sourcebook(Sourcebooks.PHB14)
class Sailor(Background):
    def __init__(self):
        super().__init__(
            name="Sailor",
            skillProf=[
                Skill.ATHLETICS,
                Skill.PERCEPTION
            ],
            toolProf=[
                Tools.NAVIGATORS_TOOLS,
                "Vehicles (Water)"
            ],
            languages=[],
            equipment=[
                "Belaying Pin (Club)",
                "Silk Rope (50 ft)",
                "Lucky Charm or Random Trinket",
                "Common Clothes",
                "pouch",
                "10 Gold"
            ],
            features=["Ship's Passage"]
        )
        
        
#Sailor (Pirate)
@registered
@sourcebook(Sourcebooks.PHB14)
class Sailor_Pirate(Sailor):
    def __init__(self):
        super().__init__()
        self.name="Sailor (Pirate)"
        self.features.remove("Ship's Passage")
        self.features.append("Bad Reputation")
        
        
#Soldier
@registered
@sourcebook(Sourcebooks.PHB14)
class Soldier(Background):
    def __init__(self):
        super().__init__(
            name="Soldier",
            skillProf=[
                Skill.ATHLETICS,
                Skill.INTIMIDATION
            ],
            toolProf=[
                "One type of gaming Set",
                "Vehicles (Land)"
            ],
            languages=[],
            equipment=[
                "Insignia of Rank",
                "Trophy from fallen enemy (Choose 1)",
                "Dice set or Playing card set",
                "common clothes",
                "pouch",
                "10 gold"
            ],
            features=["Military Rank"]
        )
        
        
#Urchin
@registered
@sourcebook(Sourcebooks.PHB14)
class Urchin(Background):
    def __init__(self):
        super().__init__(
            name="Urchin",
            skillProf=[
                Skill.SLEIGHT_OF_HAND,
                Skill.STEALTH
            ],
            toolProf=[
                Tools.DISGUISE_KIT,
                Tools.THIEVES_TOOLS
            ],
            languages=[],
            equipment=[
                "Small Knife",
                "City Map (home town)",
                "Pet Mouse",
                "Parental Momento",
                "Common Clothes",
                "Pouch",
                "10 Gold"
            ],
            features=["City Secrets"]
        )
        
        
        