# Write a program that takes as input two numbers and print the sum.
#
# Output:
# Insert the first number: 1
# Insert the second number: 2
# Sum: 3

def sum(a: int, b: int) -> int:
    return a + b

# Input the first number
num1 = int(input("Insert the first number: "))

# Input the second number
num2 = int(input("Insert the second number: "))

print("Sum:", sum(num1, num2))