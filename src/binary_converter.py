def binary_converter(decimal_value):
    return bin(decimal_value)

def main():
    decimal_value=int(input("Insert first number: "))
    print("The binary number is:",binary_converter(decimal_value)[2:])

main()