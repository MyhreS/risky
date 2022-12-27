import random

def roll_dice():
    return random.randint(1, 6)

def roll_attacker_and_defender(attacker, defender):
    attacker_rolls = []
    for i in range(attacker):
        attacker_rolls.append(roll_dice())
    attacker_rolls.sort(reverse=True)

    defender_rolls = []
    for i in range(defender):
        defender_rolls.append(roll_dice())
    defender_rolls.sort(reverse=True)
    return attacker_rolls, defender_rolls
