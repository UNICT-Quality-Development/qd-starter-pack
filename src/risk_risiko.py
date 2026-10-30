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

from random import randint

def roll_dice() -> int:
    return randint(1, 6)

def simulate_risk_fight():
    red = sorted([roll_dice() for i in range(3)])
    Blue = sorted([roll_dice() for i in range(3)])

    symbols = ["N", "M", "O"]

    print("Red dice:")
    for _ in range(len(red)):
        print(f"{red[_]} ({symbols[_]})")

    print("Blue dice:")
    for _ in range(len(Blue)):
        print(f"{Blue[_]} ({symbols[_]})")

    
    print(f"  A    B")
    for i in range(len(red)):
        if red[i] <= Blue[i]:
            print(f"{symbols[i]} {red[i]} vs {Blue[i]} Blue win")
        else:
            print(f"{symbols[i]} {red[i]} vs {Blue[i]} Red win")


if __name__ == "__main__":
    simulate_risk_fight()