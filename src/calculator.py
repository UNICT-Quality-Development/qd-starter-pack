#
#   Write a program that given two numbers as input makes the main operations.
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


def add(num1: int, num2: int) -> int:
    return num1 + num2


def subtract(num1: int, num2: int) -> int:
    return num1 - num2


def multiply(num1: int, num2: int) -> int:
    return num1 * num2


def divide(num1: int, num2: int) -> float:
    if num2 == 0:
        raise ZeroDivisionError("Divisione per zero non consentita.")
    return num1 / num2


def read_integer(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Input non valido. Inserisci un numero intero.")


def main() -> None: # pragma: no cover
    num1 = read_integer("Inserisci il numero:")
    num2 = read_integer("Inserisci il secondo numero:")

    print("Somma:", add(num1, num2))
    print("Differenza:", subtract(num1, num2))
    print("Moltiplicazione:", multiply(num1, num2))

    try:
        print("Divisione:", divide(num1, num2))
    except ZeroDivisionError:
        print("Divisione: non possibile (divisione per zero).")


if __name__ == "__main__": # pragma: no cover
    main()