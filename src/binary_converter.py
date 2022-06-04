def convert(n:int) -> str:
    res = ""
    while n != 0:
        if (n % 2) == 0:
            res += "0"
        else:
            res += "1"
            
        n = int(n/2) # senza cast a int python considera la variabile come float
    
    res = res[::-1] # inverse string
    return res


if __name__ == "__main__":
    num = int(input("Insert first number: "))
    print("The binary number is: ",convert(num))