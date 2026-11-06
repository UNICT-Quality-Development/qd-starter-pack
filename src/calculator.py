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

def sum(a: int, b: int) -> int:
    return a + b

def diff(a: int, b: int) -> int:
    return a - b

def mult(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> float:
    if b == 0:
        raise ZeroDivisionError("Impossibile dividere per zero")
    return a / b

if __name__ == "__main__":    
    a = int(input("Insert first number: "))
    b = int(input("Insert second number: "))

    print("SUM: " + str(sum(a, b)))
    print("Difference: " + str(diff(a, b)))
    print("Multiplication: " + str(mult(a, b)))
    print("Division: " + str(div(a, b)))
