# Write a program that generates a random number.

# Output:
# The random number is: 4

import random


def randomInt(a: int, b: int) -> int:
    return random.randint(a, b)


print("The random number is: ", randomInt(1, 100))
