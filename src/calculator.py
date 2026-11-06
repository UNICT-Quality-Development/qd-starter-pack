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


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float | str:
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main() -> None:  # pragma: no cover
    a = float(input("Insert first number: "))
    b = float(input("Insert second number: "))

    print("\nSUM:", add(a, b))
    print("Difference:", subtract(a, b))
    print("Multiplication:", multiply(a, b))
    print("Division:", divide(a, b))


if __name__ == "__main__":  # pragma: no cover
    main()
