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

def throwing_dice() :
  n = random.randint(1,6)
  return n
  
def tuple_dices(name):
  print(name ,"dices.. ")
  dices = []
  for x in range(3):
    dices.append(throwing_dice())
  print(dices)
  return dices


def main():
  
  atk = []
  defn = []
  tanks = ["N","M","O"]
  
  atk= tuple_dices("Red team")
  defn = tuple_dices("Blue team")
  print("")
  print("  R  VS  B")
  for x in range(3):
    if atk[x] > defn[x]:
      team_win = "red "
    elif atk[x] <= defn[x]:
      team_win = "blue"
    
    print(tanks[x],atk[x]," vs ",defn[x], "=>", team_win," team wins")
  
if __name__ == "__main__":
    main()
