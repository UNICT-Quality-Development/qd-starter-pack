# Write a program that given two numbers as input make the main operations.

# Output:
# Insert first number: 4
# Insert second number: 2

# SUM: 6
# Difference: 2
# Multiplication: 8
# Division: 2

def calculator(a: float, b: float) -> None:
    print("SUM: ", a + b)
    print("Difference: ", a - b)
    print("Multiplication: ", a * b)
    print("Division: ", a / b)

# Input the first number
a = float(input("Insert the first number: "))

# Input the second number
b = float(input("Insert the second number: "))

calculator(a, b)
