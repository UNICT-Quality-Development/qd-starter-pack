def sum(x: float, y: float) -> float:
    return x + y


def diff(x: float, y: float) -> float:
    return x - y


def mult(x: float, y: float) -> float:
    return x * y


def div(x: float, y: float) -> float | str:
    if y != 0:
        return x / y
    return "Cannot divide by 0"


if __name__ == "__main__":
    a = float(input("Enter a number "))
    b = float(input("Enter another number "))
    print(sum(a, b))
    print(diff(a, b))
    print(mult(a, b))
    print(div(a, b))
