#  Write a program that given two numbers as input make the main operations.
#  Output:
#  Insert first number: 4
#  Insert second number: 2
#  SUM: 6
#  Difference: 2
#  Multiplication: 8
#  Division: 2

def somma(a: int, b: int) -> int:
    return a + b

def differenza(a: int, b: int) -> int:
    return a - b

def moltiplicazione(a: int, b: int) -> int:
    return a * b

def divisione(a: int, b: int) -> int:
    return a / b

if __name__ == "__main__":
    x = int(input("Insert first number: "))
    y = int(input("Insert second number: "))

    print(f"SUM: {somma(x, y)}")
    print(f"Difference: {differenza(x, y)}")
    print(f"Multiplication: {moltiplicazione(x, y)}")
    print(f"Division: {divisione(x,y)}")
    