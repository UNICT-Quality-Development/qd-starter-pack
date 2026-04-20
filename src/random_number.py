#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random
import sys

def randomNumber():
    
    print("The random number is: ",random.randint(0, sys.maxsize)) 

randomNumber()