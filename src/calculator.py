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

print("\nThe sum is: ", num1+num2)
print("\nThe difference is: ", num1-num2)
print("\nThe multiplication is: ", num1*num2)

if (num2 != 0):
        print("\nThe division is:", num1/num2)
else:
    print("\nCannot divide by 0")