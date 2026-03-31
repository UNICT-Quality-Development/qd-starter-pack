#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

import random

def main():
    # -2_147_483_648 - 2_147_483_647
    print(random.randint(-2_147_483_648, 2_147_483_647))


if __name__ == "__main__":
    main()
