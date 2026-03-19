#Create final Boss battles

from Character import Character, AVAILABLE_CHARACTERS
import math
def battle(player, boss):
    print(f"--- {player.Creature} vs {boss.Creature} ---")
    player_turns_to_kill = math.ceil(boss.Health / player.Strength)
    boss_turns_to_kill = math.ceil(player.Health / boss.Strength)

    if player_turns_to_kill < boss_turns_to_kill:
        return f"{player.Creature} wins in {player_turns_to_kill} turns!"
    elif boss_turns_to_kill < player_turns_to_kill:
        return f"{boss.Creature} wins in {boss_turns_to_kill} turns!"
    else:
        return "It's a drawl! Both fell at the same time."

def battle_python():
    p1_data = AVAILABLE_CHARACTERS[4]
    boss_data = AVAILABLE_CHARACTERS[7]
    player = Character(**p1_data)
    boss = Character(**boss_data)
    print("You've run into the mighty python!")
    print("Prepare for battle.")
    result = battle(player, boss)
    print(result)


battle_python()

def battle_vampire():
    p1_data = AVAILABLE_CHARACTERS[4]
    boss_data = AVAILABLE_CHARACTERS[8]
    player = Character(**p1_data)
    boss = Character(**boss_data)
    print("You've run into the Bloodthirsty Vampire!")
    print("Prepare for battle.")
    result = battle(player, boss)
    print(result)

    battle_vampire()

    def battle_vampire():
    p1_data = AVAILABLE_CHARACTERS[4]
    boss_data = AVAILABLE_CHARACTERS[6]
    player = Character(**p1_data)
    boss = Character(**boss_data)
    print("You've run into the Ferocious dragon!")
    print("Prepare for battle.")
    result = battle(player, boss)
    print(result)

    battle_dragon()

