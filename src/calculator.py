#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#


def sum(a, b):
    return a + b


def difference(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


primo = int(input("Inserisci il primo numero: "))
secondo = int(input("Inserisci il secondo numero: "))

print(f"Sum : {sum(primo, secondo)}\n")
print(f"Difference : {difference(primo, secondo)}\n")
print(f"Multiplication : {multiplication(primo, secondo)}\n")
print(f"Division : {division(primo, secondo)}\n")
