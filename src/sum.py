def sum(a: float, b: float) -> float:
    return a+b

if __name__ == "__main__":
    number1 = float(input("Choose the first number: "))
    number2 = float(input("Choose the second number: "))

    print("Sum = ", sum(number1,number2))
