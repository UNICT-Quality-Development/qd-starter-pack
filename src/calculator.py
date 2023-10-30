"""
Write a program that given two numbers as input make the main operations.

  Output:
  Insert first number: 4
  Insert second number: 2

  SUM: 6
  Difference: 2
  Multiplication: 8
  Division: 2
*/
#include <stdio.h>
"""  

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Impossibile dividere per zero"
    return x / y

while True:
    print("Scegli un'operazione:")
    print("1. Somma")
    print("2. Sottrazione")
    print("3. Moltiplicazione")
    print("4. Divisione")
    print("5. Esci")

    choice = input("Scegli quale operazione vuoi eseguire: ")

    if choice == '5':
        print("Arrivederci!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Scelta non valida. Riprova.")
        continue

    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))

    if choice == '1':
        print("Risultato:", add(num1, num2))
    elif choice == '2':
        print("Risultato:", subtract(num1, num2))
    elif choice == '3':
        print("Risultato:", multiply(num1, num2))
    elif choice == '4':
        print("Risultato:", divide(num1, num2))
