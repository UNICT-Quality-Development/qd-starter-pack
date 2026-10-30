#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
from random import randint

def main():
    random_number = randint(1,9)
    print(f"The random number is: {random_number}")

if __name__ == "__main__":
    main()
