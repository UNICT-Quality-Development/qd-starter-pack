#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#


x = input("Insert first number: ")

try:
    x = int(x)
except:
    print("Error: The given value is not a number")
    exit(1)

print(f"The binary number is: {bin(x)}")



