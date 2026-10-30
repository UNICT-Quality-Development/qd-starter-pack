#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random

def random_number(a: int, b: int) -> int:
    return random.randint(a, b)

print("The random number is:", random_number(0, 100))