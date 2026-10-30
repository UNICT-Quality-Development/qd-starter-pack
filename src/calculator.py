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

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    try:
        num1 = float(input("Insert first number: "))
        num2 = float(input("Insert second number: "))
        print(f"\nSUM: {add(num1, num2):g}")
        print(f"Difference: {subtract(num1, num2):g}")
        print(f"Multiplication: {multiply(num1, num2):g}")
        try:
            print(f"Division: {divide(num1, num2):g}")
        except ZeroDivisionError as e:
            print(f"Division: {e}")
    except ValueError:
        print("Errore: L'input non è valido. Inserisci un numero.")
