#Write a program that given two numbers as input make the main operations.
#Output:
#Insert first number: 4
#Insert second number: 2
#SUM: 6
#Difference: 2
#Multiplication: 8
#Division: 2

def main():
    a = float(input("Insert first number: "))
    b = float(input("Insert second number: "))
    print(calculator(a, b))

def calculator(a: float, b: float) -> list:
    results = []
    results.append(f"SUM: {a + b}")
    results.append(f"Difference: {a - b}")
    results.append(f"Multiplication: {a * b}")
    results.append(f"Division: {a / b}")
    return ', '.join(results)


if __name__ == "__main__":
    main()
