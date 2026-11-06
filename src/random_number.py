#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random


def generate_random_number(minimum: int = 1, maximum: int = 10) -> int:
    return random.randint(minimum, maximum)


if __name__ == "__main__":  # pragma: no cover
    print(f"The random number is: {generate_random_number()}")
