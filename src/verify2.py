#Write a software that verifies if a number is present in a pre-defined array.
#Output example:
#Insert number 3
#The number 3 is [not] present in the array.

def foundNumber(a: int) -> bool:
    N = [5, 3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    
    for num in N:
        if num == a:
            return True
    return False 
    

def main() -> None:
    numero_da_trovare = int(input("Insert number: "))
    
    if foundNumber:
        print(f"The number {numero_da_trovare} is present in the array.")
    else:
        print(f"The number {numero_da_trovare} is [not] present in the array.")


if __name__ == "__main__":
    main()
