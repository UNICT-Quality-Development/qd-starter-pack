def verifica_presenza_numero(array, numero_da_verificare) -> bool:
    return numero_da_verificare in array

numeri = [1, 2, 3, 4, 5, 69]
numero_cercato = 4

if verifica_presenza_numero(numeri, numero_cercato):
    print(f"Il numero {numero_cercato} è presente nell'array.")
else:
    print(f"Il numero {numero_cercato} non è presente nell'array.")
