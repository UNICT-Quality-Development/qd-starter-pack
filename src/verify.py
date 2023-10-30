def verifica_presenza_numero(array, numero_da_verificare):
    if numero_da_verificare in array:
        return True
    else:
        return False

numeri = [1, 2, 3, 4, 5, 69]
numero_cercato = 3

if verifica_presenza_numero(numeri, numero_cercato):
    print(f"Il numero {numero_cercato} è presente nell'array.")
else:
    print(f"Il numero {numero_cercato} non è presente nell'array.")
