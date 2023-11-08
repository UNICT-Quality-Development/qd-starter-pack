import random

def rand()-> int:
    numero_casuale = random.randint(1, 10)
    print("Il numero casuale è:", numero_casuale)
    return numero_casuale

def main():
    rand()

if __name__ == "__main__":
    main()
