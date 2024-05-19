#   Write a program that given two numbers as input make the main operations.

#   Output:
#   Insert first number: 4
#   Insert second number: 2

#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2

x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
print("SUM: ", x+y)
print("Difference: ", x-y)
print("Multiplication: ", x*y)
try:
    print("Division: ", x/y)
except (Exception, ZeroDivisionError):
    print("Division by zero is not allowed.")
