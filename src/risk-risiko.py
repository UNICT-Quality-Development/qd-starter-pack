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

rosso = [random.randint(1, 6) for _ in range(3)]
blu = [random.randint(1, 6) for _ in range(3)]

rosso.sort(reverse=True)
blu.sort(reverse=True)

print("Dadi rossi:")
for i, val in enumerate(rosso):
    print(f"{val} ({chr(78+i)})") 

print("\nDadi blu:")
for i, val in enumerate(blu):
    print(f"{val} ({chr(78+i)})")  

print("\n  R    B")
for i in range(3):
    r = rosso[i]
    b = blu[i]
    vincitore = "rosso vince" if r > b else "blu vince"
    print(f"{chr(78+i)} {r} vs {b} => {vincitore}")
