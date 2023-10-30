#Write a software that verifies if a number is present in a pre-defined array.
#Output example:
#Insert number 3
#The number 3 is [not] present in the array.

def main():
    N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    numero_da_trovare = int(input("Insert number: "))
    found = False

    for num in N:
        if num == numero_da_trovare:
            found = True
            break
  
    if found:
        print(f"The number {numero_da_trovare} is present in the array.")
    else:
        print(f"The number {numero_da_trovare} is [not] present in the array.")


if __name__ == "__main__":
    main()
