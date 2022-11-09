#   Write a program that given two numbers as input make the main operations.
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2

def sum(x: float, y: float) -> float:
    return x+y

def difference(x: float, y: float) -> float:
    return x-y

def multiplication(x: float, y: float) -> float:
    return x*y

def division(x: float, y: float) -> float:
    return x/y

if __name__ == "__main__":
    first = float(input("insert first number: "))
    second = float(input("insert second number: "))

    print(f"SUM: {sum(first, second)}")
    print(f"Difference: {difference(first, second)}")
    print(f"Multiplication: {multiplication(first, second)}")
    print(f"Division: {division(first, second)}")
        