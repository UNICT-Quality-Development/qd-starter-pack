#
#   Write a program that, given two numbers as input, performs the main operations.
#
#   Output:
#   Enter the first number: 4
#   Enter the second number: 2
#
#   Sum: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#
# -------------------------------------------------------------------------------
from typing import Optional

# functions

def sum(a: float, b: float) -> float:
    return a + b

def diff(a: float, b: float) -> float:
    return a - b

def mult(a: float, b: float) -> float:
    return a * b

def div(a: float, b: float) -> Optional[float]:
    if b == 0:
        print("Division by 0 is not allowed.")
        return None
    return round(a / b, 2)

# inputs
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Sum: ", sum(num1, num2))
print("Difference: ", diff(num1, num2))
print("Multiplication: ", mult(num1, num2))
print("Division: ", div(num1, num2))