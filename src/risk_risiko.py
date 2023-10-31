#   Write a program that simulates a risk/risiko fight using 6 dices.

#   How does it work?
#   When a player attacks another player he uses 3 dices, the red is always the attacker and the blue is the defender.

#   You have to compare the dice with the highest number to simulate the fight.
#   N = first highest number
#   M = second highest number
#   O = third highest number

#   If the numbers are equal, the defensor (blue) wins.

#   Output:
#   Red dices:
#   6 (N)
#   3 (M)
#   2 (O)

#   Blue dices:
#   5 (N)
#   3 (M)
#   1 (O)

#     R    B
#   N 6 vs 5 => red win
#   M 3 vs 3 => blue win
#   O 2 vs 1 => red win

import random

NUMBER_OF_DICES = 3
MIN_DICE_VALUE = 1
MAX_DICE_VALUE = 6
RED_WIN_MESSAGE = "Red wins!"
BLUE_WIN_MESSAGE = "Blue wins!"

def attack()->None:
    red_dices = []
    blue_dices = []
    red_points = 0
    for i in range(NUMBER_OF_DICES):
        red_dices.append(random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE))
        blue_dices.append(random.randint(MIN_DICE_VALUE, MAX_DICE_VALUE))
    red_dices.sort(reverse=True)
    blue_dices.sort(reverse=True)
    print("Red dices:")
    for i in range(NUMBER_OF_DICES):
        print(red_dices[i])
    print("Blue dices:")
    for i in range(NUMBER_OF_DICES):
        print(blue_dices[i])
    for i in range(NUMBER_OF_DICES):
        if red_dices[i] > blue_dices[i]:
            red_points += 1
    if red_points >= 2:
        print(RED_WIN_MESSAGE)
    else:
        print(BLUE_WIN_MESSAGE)

def main():
    attack()

if __name__ == "__main__":
    main()
