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
    result = a + b
    return result

def diff(a: int, b: int) -> int:
    result = a - b
    return result

def mult(a: int, b: int) -> int:
    result = a * b
    return result

def div(a: int, b: int) -> int:
    result = a / b
    return result

a = int(input("Insert first number: "))
b = int(input("Insert second number: "))

print("SUM: " + str(sum(a, b)))
print("Difference: " + str(diff(a, b)))
print("Multiplication: " + str(mult(a, b)))
print("Division: " + str(div(a, b)))
