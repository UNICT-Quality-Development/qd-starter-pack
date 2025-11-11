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

import random

DICES_FOR_PLAYER = 3
DICES_FACES = 6
LETTERS = ["N", "M", "O"]

def random_dices_value():
    return sorted(
        [random.randint(1, DICES_FACES) for _ in range(DICES_FOR_PLAYER)],
        reverse=True
    )

def check_attack(red, blue):
    print("\n  R    B")
    for l_v, r_v, b_v in zip(LETTERS, red, blue):
        result = "blue win" if r_v <= b_v else "red win"
        print(f"{l_v} {r_v} vs {b_v} => {result}")

if __name__ == "__main__":
    red_dices = random_dices_value()
    blue_dices = random_dices_value()
    print("Red Dices: " + str(red_dices))
    print("Blue DIces: " + str(blue_dices))
    check_attack(red_dices, blue_dices)
    