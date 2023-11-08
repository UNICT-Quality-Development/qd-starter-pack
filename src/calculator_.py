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
x=""
y=""
while x.isdecimal() is False:
    x=input("Inserisci il primo numero: ")
while y.isdecimal() is False:
    y=input("inserisci il secondo numero: ")
x=int(x)
y=int(y)
print("Somma tra x e y :",x+y)
print("Differenza tra x e y :",x-y)
print("Moltiplicazione tra x e y :",x*y)
print("Differenza tra x e y:",x/y)
