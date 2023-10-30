#Write a program that given two numbers as input make the main operations.
#Output:
#Insert first number: 4
#Insert second number: 2
#SUM: 6
#Difference: 2
#Multiplication: 8
#Division: 2

def main():
    a = int(input("Insert first number: "))
    b = int(input("Insert second number: "))
    print("SUM: ", sum(a,b))
    print("Difference: ", difference(a,b))
    print("Multplication: ", multiplication(a,b))
    print("Division: ", division(a, b))

def sum(a: int, b: int) -> int:
    return a + b

def difference(a: int, b: int) -> int:
    return a - b

def multiplication(a: int, b: int) -> int:
    return a*b

def division(a: int, b: int) -> float:
    return a/b  

if __name__ == "__main__":
    main()