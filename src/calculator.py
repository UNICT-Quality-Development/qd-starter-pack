def sum(x: float, y: float) -> float:
    return x + y


def diff(x: float, y: float) -> float:
    return x - y


def mult(x: float, y: float) -> float:
    return x * y


def div(x: float, y: float) -> float | str:
    if y != 0:
        return x / y
    else:
        return "Cannot divide by 0"


if __name__ == "__main__":
    x: float = float(input("Enter a number "))
    y: float = float(input("Enter another number "))
    print(sum(x, y))
    print(diff(x, y))
    print(mult(x, y))
    print(div(x, y))
