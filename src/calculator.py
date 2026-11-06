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
    if b == 0:
        return "Error: Division by zero"
    return a / b

def main():
    a = float(input("Insert first number: "))
    b = float(input("Insert second number: "))

    print("\nSUM:", sum(a, b))
    print("Difference:", difference(a, b))
    print("Multiplication:", multiplication(a, b))
    print("Division:", division(a, b))  