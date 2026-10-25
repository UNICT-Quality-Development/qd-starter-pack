#
#   Write a program that given two numbers as input prints their sum.
#
#   Output:
#   Insert first number: 3
#   Insert second number: 5
#
#   SUM: 8
#


def sum(a: int, b: int) -> int:
    return a + b


def main() -> None:
    first = int(input("Insert first number: "))
    second = int(input("Insert second number: "))
    print(f"SUM: {sum(first, second)}")


if __name__ == "__main__":  # pragma: no cover
    main()
