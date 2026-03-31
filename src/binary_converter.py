#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#


def division(a: int) -> str:
    b = ""
    while a > 0:
        if a % 2 == 0:
            b = "0" + b
        else:
            b = "1" + b
        a = a // 2
    return f"{b}"


def carry(a: str) -> str:
    result_list = list(a)  # conversione dell'array in lista

    for i in range(len(result_list) - 1, -1, -1):  # gestione del riporto di 1
        if result_list[i] == "0":
            result_list[i] = "1"
            break
        result_list[i] = "0"

    a = "".join(result_list)
    return a


def invert(res: str) -> str:
    res = res.zfill(16)
    res = res.replace("0", "&").replace("1", "0").replace("&", "1")
    return res


if __name__ == "__main__":
    result = ""
    input = int(input("Inserisci il numero da convertire: "))

    if input == 0:
        print("0")

    elif input < 0:
        input = -input
        result = division(input)
        result = invert(result)

        print(f"Stringa modificata: {carry(result)}")
        print("Il seguente numero è calcolato con la tecnica del complemento a due.")
        print("Il risultato è rappresentato in 16 bit.")

    elif input >= 0:
        print(division(input))
