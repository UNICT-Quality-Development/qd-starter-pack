#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
from random import randint

MIN = 0
MAX = 100

def random_number(min_number: int, max_number: int) -> int:
    return randint(min_number, max_number)

print("The random number is:", random_number(MIN, MAX))
