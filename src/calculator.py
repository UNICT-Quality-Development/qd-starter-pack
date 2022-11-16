#  Write a program that given two numbers as input make the main operations.
#  Output:
#  Insert first number: 4
#  Insert second number: 2
#  SUM: 6
#  Difference: 2
#  Multiplication: 8
#  Division: 2

def somma(a: float, b: float) -> float:
    return a + b

def differenza(a: float, b: float) -> float:
    return a - b

def moltiplicazione(a: float, b: float) -> float:
    return a * b

def divisione(a: float, b: float) -> float: 
    return a / b

if __name__ == "__main__":
    x = float(input("Insert first number: "))
    y = float(input("Insert second number: "))

    print(f"SUM: {somma(x, y)}")
    print(f"Difference: {differenza(x, y)}")
    print(f"Multiplication: {moltiplicazione(x, y)}")
    print(f"Division: {divisione(x,y)}")
    