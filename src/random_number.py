#   Write a program that generates a random number.

#   Output:
#   The random number is: 4

from random import randint

MIN_RAND_VALUE = 0
MAX_RAND_VALUE = 1000

def random_number(a: int, b: int) -> int:
    return randint(a, b)

x = random_number(MIN_RAND_VALUE, MAX_RAND_VALUE)
print(x)
