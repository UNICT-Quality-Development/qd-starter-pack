# Write a software that verifies if a number is present in a pre-defined array


def verify(numbers: tuple, number: int) -> bool:
    check = "" if number in numbers else " not"
    print(f"The number is{check} in the list of numbers")

if __name__ == "__main__":
    list_numbers = ('1','2','3','4','5','6','7','8','9','10')

    number = input("Insert a number: ")

    verify(list_numbers,number)
