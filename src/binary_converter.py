def decimal_to_binary(n):
    b = ""
    while n > 0:
        if n % 2 == 0:
            b = "0" + b
        else:
            b = "1" + b
        n //= 2
    return b


n = int(input("Inserisci un numero: "))
binary_number = decimal_to_binary(n)
print("Il numero binario è:", binary_number)
