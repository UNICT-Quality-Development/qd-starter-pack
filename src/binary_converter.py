#   Write a program that given a number as input convert it in binary.
#   Output:
#   Insert first number: 8
#   The binary number is: 1000

def binary_converter(numero_s) -> int:
    numero = int(numero_s)
    binary = ''
    resto = numero
    while(resto != 0):
        binary =  str(resto % 2) + binary
        resto = int(resto / 2)
    
    return int(binary)