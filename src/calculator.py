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

num1 = float(input("Insert first number: "))
num2 = float(input("Insert second number: "))

print(f"\nSUM: {num1 + num2:g}")
print(f"Difference: {num1 - num2:g}")
print(f"Multiplication: {num1 * num2:g}")

if num2 != 0:
    print(f"Division: {num1 / num2:g}")
else:
    print("Division: Cannot divide by zero")