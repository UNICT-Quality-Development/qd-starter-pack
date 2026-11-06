#
# Write a software that verifies if a number is present in a pre-defined array.
#
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.
#
#
# #include <iostream>
# using namespace std;
#
# int main()
# {
#   // placeholder
#   int N[10] = {3, 4, 5, 1, 2, 3, 4, 9, 13, 0};
#
#   return 0;
# }

NUMBERS = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]


def is_number_present(number: int) -> bool:
    return number in NUMBERS


def main() -> None:
    try:
        input_number = int(input("Insert number: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return

    if is_number_present(input_number):
        print(f"The number {input_number} is present in the array.")
    else:
        print(f"The number {input_number} is not present in the array.")


if __name__ == "__main__":
    main()
