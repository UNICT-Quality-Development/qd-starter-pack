#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#

def dec_to_bin(num: int):
    assert num >= 0
    return dec_to_bin(num // 2) + str(num % 2) if num > 1 else str(num)

if __name__ == "__main__":
    number = int(input("Insert number: "))
    print(dec_to_bin(number))