from math import inf


def sum(a: int, b: int) -> int:
    return a + b


def sub(a: int, b: int) -> int:
    return a - b


def mul(a: int, b: int) -> int:
    return a * b


def div(a: int, b: int) -> float:
    try:
        result = a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("ERRORE!!! divisione per zero non definita.")
    return result


def mod(a: int, b: int) -> int:
    return a % b


def print_results(a: int, b: int) -> None:
    print(sum(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))
    print(mod(a, b))


def main() -> None:
    num_1 = int(input("Inserisci il primo operando: "))
    num_2 = int(input("Inserisci il secondo operando: "))
    print_results(num_1, num_2)


if __name__ == "__main__":
    main()
