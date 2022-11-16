def sum(a: int, b: int) -> int:
    return a + b


def difference(a: int, b: int) -> int:
    return a-b


def multiplication(a: int, b: int) -> int:
    return a*b


def division(a: int, b: int) -> str:
    if isinstance(a, int) or isinstance(b, int):
        try:
            return str(int(a/b))
        except ZeroDivisionError:
            return "Can't divide by 0"
    else:
        return "Make a or b integer"
