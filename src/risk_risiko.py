#
#   Write a program that simulates a risk/risiko fight using 6 dices.
#
#   How does it work?
#   When a player attacks another player he uses 3 dices, the red is always the attacker and the blue is the defender.
#
#   You have to compare the dice with the highest number to simulate the fight.
#   N = first highest number
#   M = second highest number
#   O = third highest number
#
#   If the numbers are equal, the defensor (blue) wins.
#
#   Output:
#   Red dices:
#   6 (N)
#   3 (M)
#   2 (O)
#
#   Blue dices:
#   5 (N)
#   3 (M)
#   1 (O)
#
#     R    B
#   N 6 vs 5 => red win
#   M 3 vs 3 => blue win
#   O 2 vs 1 => red win
#

import random

TURN = 3
MIN = 1
MAX = 1

def roll_dice() -> int:
    return random.randint(MIN,MAX)

def roll_3() -> list[int]:
    rolls = []
    for _ in range(TURN):
        rolls.append(roll_dice())
    return sorted(rolls, reverse=True)


def battle(red, blue) -> str:
    red_score = 0
    blue_score = 0
    for i in range(TURN):
        if red[i] > blue[i]:
            print(f"Rosso {red[i]} contro blu {blue[i]} => rosso vince")
            red_score += 1
        else:
            print(f"Rosso {red[i]} contro blu {blue[i]} => blu vince")
            blue_score += 1
    return red_score,blue_score

if __name__ == "__main__":
    red = roll_3()
    blue = roll_3()

    red = [6,3,2]
    blue = [5,3,1]
    print(f"Rosso {red}")
    print(f"blu {blue}")
    red_score,blue_score =  battle(red,blue)

    print(f"{red_score} red win")
    print(f"{blue_score} blue win")