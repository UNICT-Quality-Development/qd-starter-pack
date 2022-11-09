# Write a program that generates a random number.
# Output:
# The random number is: 4
import random;

def random_number() -> int:
  return random.randint(0,400) 

if __name__ == "__main__":

  print("The random number id: " + str( random_number() ))
  