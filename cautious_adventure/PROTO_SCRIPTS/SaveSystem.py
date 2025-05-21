import json

def save_character(character, filename):
    """Saves the character's data to a JSON file."""
    character_data = {
        "name": character.name,
        "race": character.race,
        "background": character.background,
        "alignment": character.alignment,
        "baseAttributes": character.baseAttributes,
        "levelBonuses": character.levelBonuses,
        "equipmentBonuses": character.equipmentBonuses,
        "boonBonuses": character.boonBonuses,
        "cursePenalties": character.cursePenalties,
        "attributeOverrides": character.attributeOverrides,
        "hitPoints": character.hitPoints,
        "armorClass": character.armorClass,
        "initiativeBonus": character.initiativeBonus,
        "speed": character.speed,
        "classes": character.classes,
        "levelHistory": character.levelHistory,
        "profBonus": character.profBonus,
        "feats": character.feats,
        "skills": character.skills,
        "savingThrowProf": character.savingThrowProf,
        "racialTraits": character.racialTraits,
        "languages": character.languages,
        "size": character.size
    }
    with open(filename, 'w') as f:
        json.dump(character_data, f, indent=4)
    print(f"Character '{character.name}' saved to '{filename}'")

def load_character(filename):
    """Loads character data from a JSON file and returns a Character object."""
    try:
        with open(filename, 'r') as f:
            character_data = json.load(f)
        from Character import Character
        character = Character(
            name=character_data.get("name", ""),
            race=character_data.get("race", ""),
            background=character_data.get("background", ""),
            alignment=character_data.get("alignment", ""),
            baseAttributes=character_data.get("baseAttributes", {}),
            feats=character_data.get("feats", [])
        )
        character.levelBonuses = character_data.get("levelBonuses", {})
        character.equipmentBonuses = character_data.get("equipmentBonuses", {})
        character.boonBonuses = character_data.get("boonBonuses", {})
        character.cursePenalties = character_data.get("cursePenalties", {})
        character.attributeOverrides = character_data.get("attributeOverrides", {})
        character.hitPoints = character_data.get("hitPoints", {"current": 0, "maximum": 0, "temporary": 0})
        character.armorClass = character_data.get("armorClass", 0)
        character.initiativeBonus = character_data.get("initiativeBonus", 0)
        character.speed = character_data.get("speed", 0)
        character.classes = character_data.get("classes", {})
        character.levelHistory = character_data.get("levelHistory", [])
        character.profBonus = character_data.get("profBonus", 2) # Default value if not found
        character.skills = character_data.get("skills", {})
        character.savingThrowProf = character_data.get("savingThrowProf", {})
        character.racialTraits = character_data.get("racialTraits", [])
        character.languages = character_data.get("languages", [])
        character.size = character_data.get("size", "Medium") # Default value if not found
        return character
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{filename}'.")
        return None
