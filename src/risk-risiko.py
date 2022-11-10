"""
  Write a program that simulates a risk/risiko fight using 6 dices.
  How does it work?
  When a player attacks another player he uses 3 dices, 
  the red is always the attacker and the blue is the defender.
  You have to compare the dice with the highest number to simulate 
  the fight.
  N = first highest number
  M = second highest number
  O = third highest number
  If the numbers are equal, the defensor (blue) wins.
  Output:
  Red dices:
  6 (N)
  3 (M)
  2 (O)
  Blue dices:
  5 (N)
  3 (M)
  1 (O)
    R    B
  N 6 vs 5 => red win
  M 3 vs 3 => blue win
  O 2 vs 1 => red win
"""
import random

def main():
    
    print ("Rolling attacker (red) dices.. \n")
    atk_dice_n = random.randint(1,6)
    atk_dice_m = random.randint(1,6)
    atk_dice_o = random.randint(1,6)
    attacker_dices = (atk_dice_n,atk_dice_m,atk_dice_o)
    
    # -Come creare un for con un indice per i vari confronti
    print("Red dices :")
    for x in attacker_dices:
        print(x)
    print("")
    print ("Rolling attacker (blue) dices.. \n")
    def_dice_n = random.randint(1,6)
    def_dice_m = random.randint(1,6)
    def_dice_o = random.randint(1,6)
    defender_dices = (def_dice_n,def_dice_m,def_dice_o)

    print("Blue dices :")
    for y in defender_dices:
        print(y)
        
    print ("\nR  vs  B  ")
        
    if attacker_dices[0] <= defender_dices[0]:
        print(attacker_dices[0], " vs " , defender_dices[0] , " => blue wins")
         
    elif attacker_dices[0] > defender_dices[0]:
        print(attacker_dices[0], " vs ", defender_dices[0] , "=> red wins")

# -Come creare un for con un indice per i vari confronti
#    i=[0,1,2]
#    for x in i:
#        if attacker_dices[i] <= defender_dices[i]:
#          x =  print(attacker_dices[i], " vs " , defender_dices[i] , " => blue wins")
#         
#        elif attacker_dices[i] > defender_dices[i]:
#          x =   print(attacker_dices[i], " vs ", defender_dices[i] , "=> red wins")

main()
    