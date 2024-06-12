def somma(a: float, b: float) -> float:
    return a + b

def differenza(a: float, b: float) -> float:
    return a - b

def moltiplicazione(a: float, b: float) -> float:
    return a * b

def divisione(a: float, b: float) -> float:
    if b != 0:
        return a / b
    else:
        return "Impossibile dividere per zero."

def main() -> None:
    a = float(input("Inserisci il primo numero: "))
    b = float(input("Inserisci il secondo numero: "))

    risultato_somma = somma(a, b)
    risultato_diff = differenza(a, b)
    risultato_mul = moltiplicazione(a, b)
    risultato_div = divisione(a, b)

    print(f"SOMMA: {risultato_somma}")
    print(f"DIFFERENZA: {risultato_diff}")
    print(f"MOLTIPLICAZIONE: {risultato_mul}")
    print(f"DIVISIONE: {risultato_div}")

if __name__ == "__main__":
    main()

