import random

def roll_dice():
    return random.randint(1, 6)

def roll_attacker_and_defender(attacker, defender):
    attacker_rolls = []
    for i in range(attacker):
        if i >= 3:
            break
        attacker_rolls.append(roll_dice())
    attacker_rolls.sort(reverse=True)

    defender_rolls = []
    for i in range(defender):
        if i >= 2:
            break
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

def battle(attacker, defender):
    while attacker > 0 and defender > 0:
        attacker_loss, defender_loss = find_loser(attacker, defender)
        attacker -= attacker_loss
        defender -= defender_loss
    if attacker > 0:
        return 'attacker'
    else:
        return 'defender'

def battle_simulator(attacker, defender, num_battles):
    attacker_wins = 0
    defender_wins = 0
    for i in range(num_battles):
        winner = battle(attacker, defender)
        if winner == 'attacker':
            attacker_wins += 1
        else:
            defender_wins += 1

    percent_attacker_wins = attacker_wins / num_battles * 100
    percent_defender_wins = defender_wins / num_battles * 100

    print("attacker = {} armies and defender = {} armies,\n"
          "the attacker won {}% of the time and the defender won {}% of the time in {} simulations.".format(
        attacker, defender, round(percent_attacker_wins), round(percent_defender_wins), num_battles))

    return attacker_wins, defender_wins, percent_attacker_wins, percent_defender_wins

# Get input from user and run the battle simulator
if __name__ == '__main__':
    while True:
        attacker = int(input("Enter the number of armies for the attacker: "))
        defender = int(input("Enter the number of armies for the defender: "))
        battle_simulator(attacker, defender, 1000)
        print()
        if input("Do you want to run another simulation? (y/n): ") == 'n':
            break









