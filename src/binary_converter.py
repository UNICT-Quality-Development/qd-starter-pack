#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#


def cast(x) :
    if (x//2 == 0): return "0"

    if (x % 2 == 1) : return "1" + cast(x//2)
    return "0" + cast(x//2)


x = int(input())

print(cast(x))


