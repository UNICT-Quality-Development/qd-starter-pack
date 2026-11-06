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

DICE_COUNT = 3
MIN_DICE = 1
MAX_DICE = 6
POSITION = ["N", "M", "O"]


def lancia_tre_dadi()-> list[int]:
    dadi = []
    for _ in range(0, DICE_COUNT):
        dadi.append(random.randint(MIN_DICE, MAX_DICE))
    return dadi


def print_dadi(dadi: list[int]) -> None:
    for x in range(0, DICE_COUNT):
        print(f"{dadi[x]} {POSITION[x]}")


def ordina_dadi(dadi: list[int]) -> None:
    dadi.sort(reverse = True)


def controlla_dadi(dadi_att: list[int], dadi_def: list[int]) -> list[str]:
    vincitori = []
    for x in range(0, DICE_COUNT):
        if dadi_def[x] >= dadi_att[x]:
            vincitori.append("blue")
        else:
            vincitori.append("red")
    return vincitori

if __name__ == "__main__":
    dadi_red = lancia_tre_dadi()
    dadi_blue = lancia_tre_dadi()

    #Li ordino dal più grande al più piccolo
    ordina_dadi(dadi_red)
    ordina_dadi(dadi_blue)

    print("Red dices:\n")
    print_dadi(dadi_red)
    print("Blue dices:\n")
    print_dadi(dadi_blue)



    vittorie = controlla_dadi(dadi_red, dadi_blue)

    print("\n\n")
    print("  R    B")

    for i in range(0, DICE_COUNT):
        print(f"{POSITION[i]} {dadi_red[i]} vs {dadi_blue[i]} => {vittorie[i]} win")
