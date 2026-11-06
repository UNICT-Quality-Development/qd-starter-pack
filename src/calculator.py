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

def sum(a: float, b:float) -> float:
    return float(a + b)

def sub(a:float, b:float) -> float:
    return float(a-b)

def multiple(a:float, b:float) -> float:
    return float(a*b)

def divide(a:float, b:float) -> float:
    return float(a/b)

def calculator(func: str, a: float, b:float) -> float:
    if func == "+":
        return sum(a,b)
    elif func == "-":
        return sub(a,b)
    elif func == "*":
        return multiple(a,b)
    elif func == "/":
        return divide(a,b)    
    else:
        ...