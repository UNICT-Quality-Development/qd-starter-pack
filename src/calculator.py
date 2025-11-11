def add(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float | str:
    return "You can't divide by 0" if b == 0 else a / b


print("Inserisci la x: ")
x = int(input())
print("Inserisci la y: ")
y = int(input())

print(f"sum of {x} and {y} = {add(x, y)}")
print(f"subtraction of {x} and {y} = {sub(x, y)}")
print(f"multiplication of {x} and {y} = {mul(x, y)}")
print(f"division of {x} and {y} = {div(x, y)}")
