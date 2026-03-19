from Character import Character, AVAILABLE_CHARACTERS

def select_character():
    print("--- CHOOSE YOUR CHARACTER ---")

    # 1. Display the menu with numbers
    for index, char in enumerate(AVAILABLE_CHARACTERS):
        print(f"{index + 1}. {char['Creature']} (Strength: {char['Strength']}, Health: {char['Health']})")

    # 2. Get the player's choice
    while True:
        try:
            choice = int(input("\nEnter the number of your character: "))
            if 1 <= choice <= len(AVAILABLE_CHARACTERS):
                # 3. Create the Character object from the selection
                selected_data = AVAILABLE_CHARACTERS[choice - 1]
                player_character = Character(**selected_data)

                print(f"\nYou have chosen {player_character.Creature}!")
                return player_character # Store this in your global variable
            else:
                print("Invalid number. Please choose from the list.")
        except ValueError:
            print("Please enter a valid number.")

