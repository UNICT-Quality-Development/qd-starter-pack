def somma(a, b):
    return a + b


def sottrazione(a, b):
    return a - b


def moltiplicazione(a, b):
    return a * b


def divisione(a, b):
    if b == 0:
        return "Impossibile dividere per zero."
    return a / b


while True:
    print("Opzioni:")
    print("Digita 'somma' per sommare due numeri")
    print("Digita 'sottrazione' per sottrarre due numeri")
    print("Digita 'moltiplicazione' per moltiplicare due numeri")
    print("Digita 'divisione' per dividere due numeri")
    print("Digita 'uscita' per terminare il programma")

    input_utente = input(": ")

    if input_utente == "uscita":
        break
    if input_utente in ("somma", "sottrazione", "moltiplicazione", "divisione"):
        num1 = float(input("Inserisci il primo numero: "))
        num2 = float(input("Inserisci il secondo numero: "))

        if input_utente == "somma":
            print("Risultato: ", somma(num1, num2))
        elif input_utente == "sottrazione":
            print("Risultato: ", sottrazione(num1, num2))
        elif input_utente == "moltiplicazione":
            print("Risultato: ", moltiplicazione(num1, num2))
        elif input_utente == "divisione":
            print("Risultato: ", divisione(num1, num2))
    else:
        print("Opzione non valida")
