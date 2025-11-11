#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#


def cast(x) :
    if (x == 0): return ""

    if (x % 2 == 1) : return cast(x//2) + "1"
    else : return cast(x//2) + "0"
 

x = int(input())
print(cast(x))


