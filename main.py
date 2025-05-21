from PROTO_SCRIPTS.Character import Character
#example instantiation:
if __name__ == "__main__":
    # Test Human
    humanCharacter = Character(
        name="Alice",
        race="Human",
        background="Folk Hero",
        alignment="Neutral Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=[]
    )
    print("\n--- Human Test ---")
    print(f"Name: {humanCharacter.name}")
    print(f"Race: {humanCharacter.race}")
    print(f"Base Attributes after racial bonuses: {humanCharacter.baseAttributes}")
    print(f"Racial Traits: {humanCharacter.racialTraits}")
    print(f"Speed: {humanCharacter.speed}")
    print(f"Languages: {humanCharacter.languages}")
    print(f"Size: {humanCharacter.size}")

    # Test Dwarf
    dwarfCharacter = Character(
        name="Borin",
        race="Dwarf",
        background="Guild Artisan",
        alignment="Lawful Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=[]
    )
    print("\n--- Dwarf Test ---")
    print(f"Name: {dwarfCharacter.name}")
    print(f"Race: {dwarfCharacter.race}")
    print(f"Base Attributes after racial bonuses: {dwarfCharacter.baseAttributes}")
    print(f"Racial Traits: {dwarfCharacter.racialTraits}")
    print(f"Speed: {dwarfCharacter.speed}")
    print(f"Languages: {dwarfCharacter.languages}")
    print(f"Size: {dwarfCharacter.size}")
    

    anya_to_level = Character(
        name="AnyaLevelTest",
        race="Half-Elf",
        background="Noble",
        alignment="Chaotic Good",
        baseAttributes={"STR": 10, "DEX": 10, "CON": 10, "INT": 10, "WIS": 10, "CHA": 10},
        feats=["Lucky"]
    )

    print("\n--- Anya Level Test ---")
    anya_to_level.addLevel("Fighter")
    print(f"Anya's Saving Throw Proficiencies after level 1 Fighter: {anya_to_level.savingThrowProf}")

    anya_to_level.addLevel("Wizard")
    print(f"Anya's Saving Throw Proficiencies after level 1 Wizard: {anya_to_level.savingThrowProf}")
    