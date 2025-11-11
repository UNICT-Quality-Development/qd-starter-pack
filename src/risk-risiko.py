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
red_lost = 0
blue_lost = 0
red_dices = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
red_dices.sort(reverse=True)
blue_dices = [random.randint(1,6),random.randint(1,6),random.randint(1,6)]
blue_dices.sort(reverse=True)
print("Risultati dadi attacco:",red_dices)
print("Risultati dadi difesa:",blue_dices)
for i in range(3):
    if (blue_dices[i]>=red_dices[i]):
        print(red_dices[i],"vs",blue_dices[i],": vince la difesa")
        red_lost+=1
    else:
        print(red_dices[i],"vs",blue_dices[i],": vince l'attacco")
        blue_lost+=1
print("perdite:",red_lost,"unità perse dall'attaccante,",blue_lost,"unità perse dalla difesa")
