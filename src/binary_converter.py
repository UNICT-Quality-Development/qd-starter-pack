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

def WDPG(x) :
    if (x == None) : exit(1)
    if (x<0) :
        print("1",end = '')
        x = abs(x) 
    else : print("0",end = '')
    if ((x*10)%10 == 0) : print(cast(x))
    else : print(cast(x)+"."+cast((x*10)%10))
    return 0

def checkValue(x) :
    try:
        value = float(x)
        return value
    except ValueError:
        print("Input non valido")
        #exit(1)
        return None


def main() :
    print("insert a number to cast: ")
    x = checkValue(input())
    WDPG(x)                     

if __name__ == "__main__":
    main()



