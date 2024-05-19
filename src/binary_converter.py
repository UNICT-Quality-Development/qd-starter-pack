#   Write a program that given a number as input convert it in binary.

#   Output:
#   Insert first number: 8
#   The binary number is: 1000


# The function decimal_to_binary takes a decimal number and returns a binary number in which we remove the first 2 characters that identifies a binary digit (0b).
def decimal_to_binary(decimal_number):
    return bin(decimal_number)[2:]


input_number = int(input("Insert first number: "))

print("The binary number is: " + decimal_to_binary(input_number))
