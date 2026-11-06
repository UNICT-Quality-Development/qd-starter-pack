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

import sys


def sum(a: int, b: int) -> int:
    return a + b

def subtract(a: int, b: int) -> int:
    return a - b

def multiply(a: int, b: int) -> int:
    return a * b

def divide(a: int, b: int) -> float:
    if b == 0:
        return None
    return a / b

def main() -> None:
    try:
        a = int(input("Insert first number: "))
        b = int(input("Insert second number: "))
    except ValueError:
        print("Please insert valid numbers.")
        sys.exit(1)

    print("SUM", sum(a,b))
    print("Difference", subtract(a,b))
    print("Multiplication", multiply(a,b))
    print("Division", divide(a,b))

if __name__ == "__main__": #pragma: no cover
    main()
