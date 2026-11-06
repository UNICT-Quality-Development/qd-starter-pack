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

def func_sum(x: int, y: int) -> int:
    return x + y


def difference(x: int, y: int) -> int:
    return x - y


def multiplication(x: int, y: int) -> int:
    return x * y


def division(x: int, y: int) -> int:
    return int(x / y)


def main() -> None:
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))

    print(f"SUM: {func_sum(num1, num2)}")
    print(f"Difference: {difference(num1, num2)}")
    print(f"Multiplication: {multiplication(num1, num2)}")
    print(f"Division: {division(num1, num2)}")


if __name__ == "__main__":
    main()
