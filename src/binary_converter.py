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

def main() :
    print("insert a number to cast: ")
    x = float(input())
    if (x<0) :
        print("1",end = '')
        x = abs(x) 
    else : print("0",end = '')
    if ((x*10)%10 == 0) : print(cast(x))
    else : print(cast(x)+"."+cast((x*10)%10))

if __name__ == "__main__":
    main()



