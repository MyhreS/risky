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

def find_loser(attacker, defender):
    attacker_rolls, defender_rolls = roll_attacker_and_defender(attacker, defender)
    attacker_loss = 0
    defender_loss = 0
    for attacker_roll, defender_roll in zip(attacker_rolls, defender_rolls):
        if attacker_roll > defender_roll:
            defender_loss += 1
        else:
            attacker_loss += 1
    return attacker_loss, defender_loss









