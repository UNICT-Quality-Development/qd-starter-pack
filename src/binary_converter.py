def BinaryConverter(num : int) -> int:

    if num > 1:
        BinaryConverter(num // 2)
    print (num % 2, end = '')

x = input("Insert the first number: ")
print ("The binary number is: ", end='')
BinaryConverter(int(x))
print("")
