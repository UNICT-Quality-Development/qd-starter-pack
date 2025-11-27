"""Scrivere in python un esercizio che prenda un numero da 1 a 7 e restituisca il giorno della settimana corrispondente.
Utilizzare un array per memorizzare i nomi dei giorni della settimana invece di utilizzare una serie di istruzioni if/else if.

"""


def giorno_della_settimana(n: int) -> str:

    match n:
        case 1:
            return "Lunedì"
        case 2:
            return "Martedì"
        case 3:
            return "Mercoledì"
        case 4:
            return "Giovedì"
        case 5:
            return "Venerdì"
        case 6:
            return "Sabato"
        case 7:
            return "Domenica"
        case _:
            return "--"


if __name__ == "__main__":

    s = input("Scegli un giorno della settimana: ")
    print("Il girono della settimana scelto: è ", giorno_della_settimana(int(s)))
