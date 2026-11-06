#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

from random import randint

MIN_RANDOM_NUMBER = 1
MAX_RANDOM_NUMBER = 10

def get_random_number() -> int:
    return randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER)


if __name__ == "__main__": # pragma: no cover
    print(f"The random number is: {get_random_number()}")
