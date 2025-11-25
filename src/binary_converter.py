#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#

def binary_converter(number: int) -> str:
    if number == 0:
        return "0"
    binary_digits = []
    while number > 0:
        binary_digits.append(str(number % 2))
        number //= 2
    binary_digits.reverse()
    return ''.join(binary_digits)

if __name__ == "__main__":
    num = int(input("Insert the number: "))
    print(f"The binary number is: {binary_converter(num)}")
    
    