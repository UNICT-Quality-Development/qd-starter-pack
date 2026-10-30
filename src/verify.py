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

NUMBERS: list[int] = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]


def in_array(number: int) -> bool:
    return number in NUMBERS


if __name__ == "__main__":
    try:
        num = int(input("Insert number: "))
        is_in_array: bool = in_array(num)
        not_str: str = "" if is_in_array else "not "
        print(f"The number {num} is {not_str}present in the array.")
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
