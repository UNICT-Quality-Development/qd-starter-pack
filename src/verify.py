import random

def genera_array_numeri_random(n, minimo, massimo):
    return [random.randint(minimo, massimo) for _ in range(n)]

n = 10  # Numero di elementi nell'array
minimo = 1  # Il valore minimo che può essere generato
massimo = 15  # Il valore massimo che può essere generato

array_numeri_random = genera_array_numeri_random(n, minimo, massimo)

numero_da_cercare = int(input('Inserisci il numero da cercare: '))

trovato = False

for num in array_numeri_random:
    if num == numero_da_cercare:
        trovato = True
        break

if trovato:
    print(f"Il numero {numero_da_cercare} è presente nell'array.")
else:
    print(f"Il numero {numero_da_cercare} non è presente nell'array.")
