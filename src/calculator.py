#Write a program that given two numbers as input make the main operations.
#
#Output:
#Insert first number: 4
#Insert second number: 2
#
#SUM: 6
#Difference: 2
#Multiplication: 8
#Division: 2

def sum(a:int, b:int) -> int:
    return int(a)+int(b)

def dif(a:int, b:int) -> int:
    return int(a)-int(b)

def mul(a:int, b:int) -> int:
    return int(a)*int(b)

def div(a:int, b:int) -> int:
    return int(a)/int(b)

if __name__ == '__main__':
    a = input("Insert the first number: ")
    b = input("Insert the second number: ")

    print ("Sum: ", sum(a, b))
    print ("Difference: ", dif(a, b))
    print ("Multiplication: ", mul(a, b))
    print ("Division: ", div(b, a))
