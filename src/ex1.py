def giorno_della_settimana():
    week = int(input("Inserisci il numero della settimana (1-7): "))

    switch = {
        1: "Lunedì",
        2: "Martedì",
        3: "Mercoledì",
        4: "Giovedì",
        5: "Venerdì",
        6: "Sabato",
        7: "Domenica"
    }

    day = switch.get(week, "Input non valido! Inserisci un numero della settimana tra 1 e 7.")
    
    return day

print(giorno_della_settimana())
