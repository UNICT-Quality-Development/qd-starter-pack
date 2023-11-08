def BinaryConverter(num : int) -> int:

    if num > 1:
        BinaryConverter(num // 2)
    print (num % 2, end = '')

if __name__ == '__main__':
    x = input("Insert the number: ")
    print ("The binary number is: ", end='')
    BinaryConverter(int(x))
    print("")
