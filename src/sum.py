# Write a program that takes as input two numbers and print the sum.

# Output:
# Insert the first number: 1
# Insert the second number: 2
# Sum: 3


def Sum(a: int, b: int) -> int:
    return a + b


FirstNumber = int(input("Insert the first number : "))

SecondNumber = int(input("Insert the second number : "))

print("Sum :", Sum(FirstNumber, SecondNumber))
