from typing import List
#   Write a program that given two numbers as input make the main operations.

#   Output:
#   Insert first number: 4
#   Insert second number: 2

#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2

def sum (x: float, y: float) -> float:
    return x + y

def difference (x: float, y: float) -> float:
    return x - y

def multiplication (x: float, y: float) -> float:
    return x * y

def division (x: float, y: float) -> float:
    return x / y

def all(x: float, y: float) -> List[float]:
    return [
        sum(x,y),
        difference(x,y),
        multiplication(x,y),
        division(x,y)
    ]