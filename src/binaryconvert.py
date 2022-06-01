#  Write a program that given a number as input convert it in binary.
#  Output:
#  Insert first number: 8
#  The binary number is: 1000

import math

def ConvertiInBinario(n):
    valore=" "
    while n>0:
        
        if n%2==0:
            valore='0'+valore
            
        else:
            valore='1'+valore
            
        n=int(n/2)
    return valore
    
if __name__ == "__main__":
    n=int(input('inserisci il valore del numero da inserire:'))
    print(ConvertiInBinario(int(n)))
    