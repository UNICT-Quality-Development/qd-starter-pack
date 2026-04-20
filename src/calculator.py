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


x = input("Insert first number: ")

try:
    x = int(x)
except:
    print("Error: The given value is not a number")
    exit(1)

y = input("Insert second number: ")

try:
    y = int(y)
except:
    print("Error: The given value is not a number")
    exit(1)

print(f"\nSUM: {x+y}\nDifference: {x-y}\nMultiplication: {x*y}")

if y == 0:
    print("Division: Warnings: Impossible to divide by 0")
    exit(0)

print(f"Division: {int(x/y)}")
