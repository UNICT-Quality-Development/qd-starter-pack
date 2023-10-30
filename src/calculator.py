#   Write a program that given two numbers as input make the main operations.

#   Output:
#   Insert first number: 4
#   Insert second number: 2

#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2

first_number = int(input("Insert first number: "))
second_number = int(input("Insert second number: "))
print("SUM: ", first_number+second_number)
print("Difference: ", first_number-second_number)
print("Multiplication: ", first_number*second_number)
try:
    print("Division: ", first_number/second_number)
except ZeroDivisionError:
    print("You cannot divide by 0")