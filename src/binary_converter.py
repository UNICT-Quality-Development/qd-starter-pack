def binary_converter(decimal_num: int) -> str:
    converted = ""
    while decimal_num > 0:
        if decimal_num % 2 == 0:
            converted += "0"  # concateno perché sì. (dai è più compatto)
        else:
            converted += "1"
        decimal_num //= 2
    return converted[::-1]  # Sì stefano lo so è bruttissima questa cosa <3


# Stringhe per testare in loco:
# num = int(input("Mbare dammi un numero bro forza:"))
# print(binary_converter(num))
