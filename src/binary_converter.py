def dec_bin(num: int) -> int:
    binary = ''
    while num>0:
        if num%2 == 0:
            binary = '0' + binary
        else:
            binary = '1' + binary
        num = int(num/2)
    return binary

if __name__ == "__main__":
    number = int(input("Insert first number: "))
    print("The binary number is: "+dec_bin(number))