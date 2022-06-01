"""
/*
  Write a program that generates a random number.
  Output:
  The random number is: 4
*/"""

from random import random

def random_num()->int:
    return int(random()*100)

def main()->None:
    print("The random number is: ",random_num())

main()
    