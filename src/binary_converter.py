def print_binary_number(n: int) ->None:
    if n<=1:
        print(n, end="")
        return
    print_binary_number(n//2)
    print(n&1, end="")
if __name__ == '__main__':
	k=int(input("Inserisci un numero\n"))
	print_binary_number(k)
	print()
