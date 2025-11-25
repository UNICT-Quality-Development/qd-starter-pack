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
dice_number = 3

def risiko():
    try:
        n_dices_red = int(input("[RED]  : how many dices would you like to use? "))
        n_dices_blue = int(input("[BLUE] : how many dices would you like to use? "))
    except:
        print("Invalid input! make sure to use a number greater then 0!")
        return
 
    if (n_dices_red <=0 or n_dices_blue <=0):
        print("Number of dices less then zero are not acceptable")
        return


    red_dices=list(range(n_dices_red))
    blue_dices=list(range(n_dices_blue))

    throw_dices(red_dices)
    throw_dices(blue_dices)

    for i in range(min(n_dices_blue,n_dices_red)):
        if blue_dices[i] >= red_dices[i]:
            print("Blue won battle number ",i+1," [ R(",red_dices[i],") , B(",blue_dices[i],") ]")
        else:
            print("Red won battle number ",i+1," [ R(",red_dices[i],") , B(",blue_dices[i],") ]")


def throw_dices(dices):
    for i in range (len(dices)):
        dices.append(random.randint(1,6))
    dices.sort(reverse=True)

risiko()

        