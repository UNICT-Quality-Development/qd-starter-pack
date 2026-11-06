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

def sum(n1: float, n2: float) -> float:
    return n1 + n2

def difference(n1: float, n2: float) -> float:
    return n1 - n2

def multiplication(n1: float, n2: float) -> float:
    return n1 * n2

def division(n1: float, n2: float) -> float:
    return n1 / n2

if __name__ == "__main__":
    first_number = float(input("Insert first number: "))
    second_number = float(input("Insert second number: "))

    print("SUM: ", sum(first_number, second_number))
    print("Difference: ", difference(first_number, second_number))
    print("Multiplication: ", multiplication(first_number, second_number))
    print("Division: ", division(first_number, second_number))