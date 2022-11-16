
#   Write a program that given two numbers as input make the main operations.

#   Output:
#   Insert first number: 4
#   Insert second number: 2

#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2

def sum (x: int, y: int) -> int:
    return x + y

def difference (x: int, y: int) -> int:
    return x - y

def multiplication (x: int, y: int) -> int:
    return x * y

def division (x: int, y: int) -> float:
    return x / y

def all(x: int, y: int) -> None:
    return [
        sum(x,y),
        difference(x,y),
        multiplication(x,y),
        division(x,y)
    ]
