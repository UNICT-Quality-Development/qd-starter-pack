"""
  Write a program that given a number as input convert it in binary.

  Output:
  Insert first number: 8
  The binary number is: 1000
"""


res = ""
def to_binary(n: int) -> str:
    global res
    res = ""
    while (n):
        if n%2 == 0:
            res += '0'
        else:
            res += '1'
        n >>= 1

    return res[::-1]

if __name__ == "__main__":
    n = int(input("Insert first number: "))
    print("The binary number is: ", to_binary(n))
