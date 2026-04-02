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

def sum(x, y):
    return "SUM: " + str(x + y)

def sub(x, y):
    return "Difference: " + str(x - y)

def mul(x, y):
    return "Multiplication " + str(x * y)

def div(x, y):
    if y == 0:
        return "divisione per 0 non permessa"
    return "Division: " + str(x / y)


x = float(input("Insert first number: "))
y = float(input("Insert second number: "))

print(sum(x, y))
print(sub(x, y))
print(mul(x, y))
print(div(x, y))

