#
# Write a software that verifies if a number is present in a pre-defined array.
#
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.
#
pre_defined_array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]


def user_insert(mess: str) -> int:
    return int(input(mess))


def search_value(value: int) -> bool:
    if value in pre_defined_array:
        print("The element " + str(value) + " is present in the array")
        return True

    print("The element " + str(value) + " is not present in the array")
    return False


if __name__ == "__main__":
    user_input = user_insert("Inserisci: ")
    search_value(user_input)
