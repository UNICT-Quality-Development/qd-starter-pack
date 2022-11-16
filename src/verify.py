def verify(numbers: tuple[str, ...], number: str) -> str:
    return "" if number in numbers else " not"


def main():
    list_numbers = ('1','2','3','4','5','6','7','8','9','10')

    number = input("Insert a number: ")
    check = verify(list_numbers,number)
    
    print(f"The number is{check} in the list of numbers")

if __name__ == "__main__":
    main()
