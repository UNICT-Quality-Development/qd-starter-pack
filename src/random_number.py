# Write a program that generates a random number.
#
# Output:
# The random number is: 4

from random import randint

MIN_NUMBER = 1
MAX_NUMBER = 10

random_number = randint(MIN_NUMBER, MAX_NUMBER)

print("The random number is:", random_number)
