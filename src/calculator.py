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


def addizione(num1: float, num2: float) -> float:
    return num1 + num2


def sottrazione(num1: float, num2: float) -> float:
    return num1 - num2


def moltiplicazione(num1: float, num2: float) -> float:
    return num1 * num2


def divisione(num1: float, num2: float) -> float | str:
    if num2 == 0:
        return "incalcolabile. Divisione per zero non consentita."
    return num1 / num2


def prendi_input() -> tuple[float, float]:
    num1 = float(input("Inserisci il primo numero: "))
    num2 = float(input("Inserisci il secondo numero: "))
    return num1, num2


if __name__ == "__main__":
    a, b = prendi_input()

    print("La somma è", addizione(a, b))
    print("La differenza è", sottrazione(a, b))
    print("Il prodotto è", moltiplicazione(a, b))
    print("Il quoziente è", divisione(a, b))
