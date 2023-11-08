def BinaryConverter(num):
    if num == 0:
        return "0"
    r=""
    while num > 0:
        if num % 2 == 0:
            r = "0" + r
        else:
            r = "1" + r
        num //= 2
    return r

if __name__ == '__main__':
    x = input("Insert the number: ")
    print ("The binary number is: " + BinaryConverter(int(x)))
    print("")
