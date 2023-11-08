def binary_converter(decimal_num: int) -> str:
    converted = ""
    if decimal_num == 0:
        return "0"
    if decimal_num < 0:
        raise ValueError("Solo numeri positivi sono permessi")
    while decimal_num > 0:
        if decimal_num % 2 == 0:
            converted += "0"  # concateno perché sì. (dai è più compatto)
        else:
            converted += "1"
        decimal_num //= 2
    return converted[::-1]  # Sì stefano lo so è bruttissima questa cosa <3


def main():
    n = int(input("Inserisci un numero: "))
    binary_numer = binary_converter(n)
    print("Il tuo numero in binario è:", binary_numer)


if __name__ == "__main__":
    main()
