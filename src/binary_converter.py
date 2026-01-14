#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#

def get_operands():
    print("Enter the integer:")
    n = int(input())
    return n

def binary_converter(n):
    x = ''
    if n == 0:
        print("0")
        return
    while n > 0:
        x = str(n % 2) + x
        n = int(n / 2)
    print("The number is:", x)

n = get_operands()
binary_converter(n)
