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

def sum(x: int, y: int) -> int:
    return x + y

def diff(x: int, y: int) -> int:
    return x - y

def mult(x: int, y: int) -> int:
    return x * y

def div(x: int, y: int) -> float:
    if y == 0:
        raise ZeroDivisionError("Impossibile dividere per zero")
    return x / y

if __name__ == "__main__":
    a = int(input("Insert first number: "))
    b = int(input("Insert second number: "))

    print("SUM: " + str(sum(a, b)))
    print("Difference: " + str(diff(a, b)))
    print("Multiplication: " + str(mult(a, b)))
    print("Division: " + str(div(a, b)))
