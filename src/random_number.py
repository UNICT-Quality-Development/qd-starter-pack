#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random
def generator_number():
 number = int(input("Insert the end of the interval: "))
 number = random.randint(1, number)
 print(""The random number between 1 and", n, "is:" ", number)	
 return number
generator_number()
