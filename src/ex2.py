"""Scrivere in python un esercizio che prenda un numero da 1 a 7 e restituisca il giorno della settimana corrispondente.
Utilizzare un array per memorizzare i nomi dei giorni della settimana invece di utilizzare una serie di istruzioni if/else if.
"""

# Giorni della settimana memorizzati in un array
giorni_settimana = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]
# Input dell'utente
numero_settimana = int(input("Enter week number (1-7): "))
# Verifica se l'input è valido e stampa il giorno corrispondente
if 1 <= numero_settimana <= 7:
    print(giorni_settimana[numero_settimana - 1])  # Sottrai 1 per l'indice dell'array
else:
    print("Invalid input! Please enter week number between 1-7.")
