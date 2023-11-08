def somma(a, b):
    return a + b


def sottrazione(a, b):
    return a - b


def moltiplicazione(a, b):
    return a * b


def divisione(a, b):
    if b == 0:
        raise ValueError("Il denominatore deve essere non nullo")
    return a / b




def main():
    num1 = int(input("Inserisci un numero: "))
    num2 = int(input("Inserisci un numero: "))
    print("Risultato: ", somma(num1, num2))
    print("Risultato: ", sottrazione(num1, num2))
    print("Risultato: ", moltiplicazione(num1, num2))
    print("Risultato: ", divisione(num1, num2))
    print("Opzione non valida")

if __name__ == "__main__":
    main()