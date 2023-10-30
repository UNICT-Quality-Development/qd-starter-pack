""" Write a program that given a number as input convert it in binary.

  Output:
  Insert first number: 8
  The binary number is: 1000 """


def print_binary_number(n: int) -> None:
    if n<=1:
        print(n, end="")
        return
    print_binary_number(n//2)
    print(n&1, end="")
    
k=int(input("Inserisci un numero\n"))
print_binary_number(k)
print()
