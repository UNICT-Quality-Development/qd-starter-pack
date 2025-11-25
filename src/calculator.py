def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float | str:
    return "You can't divide by 0" if b == 0 else a / b


if __name__ == "__main__":
    x = int(input("Insert first number: "))
    y = int(input("Insert second number: "))

    print(f"Sum of {x} and {y} = {add(x, y)}")
    print(f"Subtraction of {x} and {y} = {sub(x, y)}")
    print(f"Multiplication of {x} and {y} = {mul(x, y)}")
    print(f"Division of {x} and {y} = {div(x, y)}")
