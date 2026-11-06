#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

from random import randint


def get_random_number() -> int:
    return randint(1, 10)


if __name__ == "__main__":
    print(f"The random number is: {get_random_number()}")
