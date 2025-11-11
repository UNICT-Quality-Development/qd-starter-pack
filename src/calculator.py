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
print("Enter two numbers:")
x = float(input())
print("Enter number B:")
y = float(input())

print(f"You choose {x} ==and {y}")

def sum(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int | str:
    return "You can't divide by zero" if b == 0 else a / b

result = round(mul(x, y), 2)
print(result)