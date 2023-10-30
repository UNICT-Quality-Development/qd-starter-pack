"""
 Write a program that given two numbers as input make the main operations.

 Output:
 Insert first number: 4
 Insert second number: 2

 SUM: 6
 Difference: 2
 Multiplication: 8
 Division: 2
"""

primo = input("Inserisci il primo numero: ")
secondo = input("Inserisci il secondo numero: ")

x = int(primo)
y = int(secondo)

Somma = x+y
Differenza = x-y
Moltiplicazione = x*y
Divisione = x/y

somma = str(Somma)
differenza = str(Differenza)
moltiplicazione = str(Moltiplicazione)
divisione = str(Divisione)

print ("SUM:" + somma)
print ("Difference:" + differenza)
print ("Multipication:" + moltiplicazione)
print ("Division:" + divisione)
