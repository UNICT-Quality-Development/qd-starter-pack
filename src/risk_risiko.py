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

def lanciaTreDadi()-> int:
    dadi = []
    for _ in range(0,3):
        dadi.append(random.randint(1,6))
    return dadi

dadi_def = lanciaTreDadi()
dadi_att = lanciaTreDadi()

#Li ordino dal più grande al più piccolo
dadi_def.sort(reverse=True)
dadi_att.sort(reverse=True)

support = ["N","M","O"]

print("Red dices:")
for x in range(0,3):
    print(f"{dadi_att[x]} {support[x]}")


print("Blue dices:")
for x in range(0,3):
    print(f"{dadi_def[x]} {support[x]}")

print("\n\n")
print("  R    B")
for x in range(0,3):
    if dadi_def[x] >= dadi_att[x]:
        print(f"{support[x]} {dadi_att[x]} vs {dadi_def[x]} => blue win")
    else:
        print(f"{support[x]} {dadi_att[x]} vs {dadi_def[x]} => red win")
