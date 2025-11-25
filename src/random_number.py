#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random
import sys


def random_number() -> int:
    return random.randint(0, sys.maxsize)


if __name__ == "__main__":
    print(random_number())
