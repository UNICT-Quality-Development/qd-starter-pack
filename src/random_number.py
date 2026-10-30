#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

import random 

range_min = input("Inserisci il numero minimo dell'intervallo: ")
range_max = input("Inserisci il numero massimo dell'intervallo: ")

rnd_number = random.randint(int(range_min), int(range_max))
print(f"Il numero generato casualmente è: {rnd_number}")
