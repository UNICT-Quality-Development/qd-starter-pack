def sum(a: int, b: int) -> int:
    return a + b


def diff(a: int, b: int) -> int:
    return a - b


def mol(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> int:
    if b == 0:
        return "Error: can't divide by 0."
    return a // b


def main() -> None:
    a = int(input("Insert first number: "))
    b = int(input("Insert second number: "))

    print("SUM:", sum(a, b))
    print("Difference:", diff(a, b))
    print("Moltiplication:", mol(a, b))
    print("Division:", div(a, b))

    return None


if __name__ == "__main__":
    main()
