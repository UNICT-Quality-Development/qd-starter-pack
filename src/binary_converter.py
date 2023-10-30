#   Write a program that given a number as input convert it in binary.

#   Output:
#   Insert first number: 8
#   The binary number is: 1000

decimal_number = int(input("Insert first number: "))
print("The binary number is: " + bin(decimal_number)[2:])