#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#
import random
def generator_number():
 number = int(input("Inserisci un numero: "))
 number = random.randint(1, number)
 print("Il numero casuale e': ", number)	
 return number
generator_number()
