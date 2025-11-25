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
import enum

class OperationType(enum.Enum):
    SUM = 1
    DIFFERENCE = 2
    MULTIPLICATION = 3
    DIVISION = 4

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Error: Division by zero")
    
def operation(a, b, op: OperationType):
    if op == OperationType.SUM:
        return sum(a, b)
    elif op == OperationType.DIFFERENCE:
        return difference(a, b)
    elif op == OperationType.MULTIPLICATION:
        return multiplication(a, b)
    elif op == OperationType.DIVISION:
        return division(a, b)
    else:
        raise ValueError("Invalid operation")
    
if __name__ == "__main__":
    num1 = float(input("Insert first number: "))
    num2 = float(input("Insert second number: "))
    
    print(f"SUM: {operation(num1, num2, OperationType.SUM)}")
    print(f"Difference: {operation(num1, num2, OperationType.DIFFERENCE)}")
    print(f"Multiplication: {operation(num1, num2, OperationType.MULTIPLICATION)}")
    print(f"Division: {operation(num1, num2, OperationType.DIVISION)}")