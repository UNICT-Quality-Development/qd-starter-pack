# Write a program that takes as input two numbers and print the sum.

# Output:
# Insert the first number: 1
# Insert the second number: 2
# Sum: 3


def Sum(a: int, b: int) -> int:
    return a + b


a = int(input("Insert the first number : "))

b = int(input("Insert the second number : "))

print("Sum :", Sum(a, b))
