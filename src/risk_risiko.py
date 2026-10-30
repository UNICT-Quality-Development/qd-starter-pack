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
def print_dices(player: str, dices: list[int]) -> None:
  n, m, o = dices
  print(f"{player} dices:")
  print(f"{n} (N)")
  print(f"{m} (M)")
  print(f"{o} (O)")

def print_results(red_wins: bool, results: list[bool], red: list[int], blue: list[int]) -> None:
  print_dices('Red', red)
  print_dices('Blue', blue)
  winner_per_round = [ "red" if result else "blue" for result in results  ]
  winner = "red" if sum(results) > 1 else "blue"

  output_text = f"""
  R    B
N {red[0]} vs {blue[0]} => {winner_per_round[0]} wins
M {red[1]} vs {blue[1]} => {winner_per_round[1]} wins
O {red[2]} vs {blue[2]} => {winner_per_round[2]} wins

winner is {winner}
  """
  
  print(output_text)


def risiko(red: list[int], blue: list[int]) -> (bool, list[bool]):
  """
  Plays a risiko match between red and blue player
  :param red an array of 3 integers representing the dices drawn by the red player
  :param blue an array of 3 integers representing the dices drawn by the blue player
  :returns a tuple 
  """
  assert(len(red) == 3 and len(blue) == 3)
  results = list( x != y for (x,y) in zip(red, blue))

  red_wins = sum(results) > 1

  return ( red_wins, results )


if __name__ == '__main__':
  import random

  random.seed(None)

  red = list(sorted([ random.randint(1,6) for i in range(3)], reverse=True))
  blue = list(sorted([ random.randint(1,6) for i in range(3)], reverse=True))


  red_wins, results = risiko(red, blue)

  print_results(red_wins, results, red, blue)