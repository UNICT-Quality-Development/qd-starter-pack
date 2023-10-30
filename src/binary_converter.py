def print_binary_number(n: int):
    if(n<=1):
            print(n, end="")
            return
    print_binary_number(n//2)
    print(n&1, end="")
    return

k=int(input("Inserisci un numero\n"))
print_binary_number(k)
print()
