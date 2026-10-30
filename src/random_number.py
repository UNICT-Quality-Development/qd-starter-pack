#
#   Write a program that generates a random number.
#
#   Output:
#   The random number is: 4
#

from random import randint

def gen_random_number():
    try:
        range_min = int(input("Inserisci il numero minimo dell'intervallo: "))
        range_max = int(input("Inserisci il numero massimo dell'intervallo: "))
    except ValueError:
        print("Per favore, inserisci un numero valido.")
        return None

    if range_min > range_max:
        print("Il numero minimo non può essere maggiore del numero massimo.")
        return None

    return randint(int(range_min), int(range_max))

if __name__ == "__main__":
    val = gen_random_number()
    if val is not None:
        print(f"Il numero generato casualmente è: {val}")
    else:
        print("Non è stato possibile generare un numero casuale a causa di input non validi.")