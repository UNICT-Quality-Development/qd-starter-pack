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
def sum(num1: float, num2: float) -> float:
    return float(num1) + float(num2)


def difference(num1: float, num2: float) -> float:
    return float(num1) - float(num2)


def multiplication(num1: float, num2: float) -> float:
    return float(num1) * float(num2)


def division(num1: float, num2: float) -> float:
    return float(num1) / float(num2) if num2 != 0 else 0


def main() -> None:
    num1 = float(input("Insert first number: "))
    num2 = float(input("Insert second number: "))

    sum_result = sum(num1, num2)
    difference_result = difference(num1, num2)
    multiplication_result = multiplication(num1, num2)
    division_result = division(num1, num2)

    print(f"\nSUM: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Multiplication: {multiplication_result}")
    print(f"Division: {division_result}")


if __name__ == "__main__":
    main()
