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

numbers = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

try:
    input_number = int(input("Insert number: "))
    is_present = False

    for number in numbers:
        if input_number == number:
            is_present = True
            break

    if is_present:
        print(f"The number {input_number} is present in the array.")
    else:
        print(f"The number {input_number} is not present in the array.")
except ValueError:
    print("Invalid input! Please enter an integer.")
