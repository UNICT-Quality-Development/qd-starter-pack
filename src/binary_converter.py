#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#
x = int(input("Insert first number: "))
# x = int(input())

def decimal_to_binary(num):
    y = "1"
    while(num != 1):
        y += str(int(num%2))
        num = int(num / 2)
    return y

print("The binary number is: " + decimal_to_binary(x))
