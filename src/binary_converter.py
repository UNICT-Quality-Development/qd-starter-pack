def decimal_to_binary(n):
    if n < 0:
        raise ValueError("Il numero deve essere positivo")
    if n == 0:
        return "0"
    b = ""
    while n > 0:
        if n % 2 == 0:
            b = "0" + b
        else:
            b = "1" + b
        n //= 2
    return b

def main():
    n = int(input("Inserisci un numero: "))
    binary_number = decimal_to_binary(n)
    print("Il numero binario è:", binary_number)

if __name__ == "__main__":
    main()

