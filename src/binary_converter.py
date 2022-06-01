'''
  Write a program that given a number as input convert it in binary.
  Output:
  Insert first number: 8
  The binary number is: 1000

'''

import math

def bin_conv(dec : int) -> str:
    numbin : str = ""
    i = int(math.log(dec, 2)+1)
    while i > 0:
        numbin = str(dec%2) + numbin
        dec = dec//2
        i -= 1
    return numbin


if __name__ == "__main__":
    print(bin_conv(255))
    
