import random

def genera_array_numeri_random(numero_elementi, valore_minimo, valore_massimo):
    return [random.randint(valore_minimo, valore_massimo) for _ in range(numero_elementi)]

numero_elementi = 10  # Numero di elementi nell'array
valore_minimo = 1  # Il valore minimo che può essere generato
valore_massimo = 15  # Il valore massimo che può essere generato

array_numeri_random = genera_array_numeri_random(numero_elementi, valore_minimo, valore_massimo)

numero_da_cercare = int(input('Inserisci il numero da cercare: '))

trovato = False

for numero in array_numeri_random:
    if numero == numero_da_cercare:
        trovato = True
        break

if trovato:
    print(f"Il numero {numero_da_cercare} è presente nell'array.")
else:
    print(f"Il numero {numero_da_cercare} non è presente nell'array.")
