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

def get_operands():
    global x, y
    print("Get first operand:")
    x = int(input())
    print("Get second operand")
    y = int(input())

def calculator(op1, op2):
    print(op1, "+", op2, "=", op1+op2)
    print(op1, "-", op2, "=", op1-op2)
    print(op1, "x", op2, "=", op1*op2)
    print(op1, "/", op2, "=", op1/op2)

get_operands()
calculator(x, y)
    