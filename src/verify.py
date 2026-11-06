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


def is_in_array(item: int, array: list[int]) -> bool:
    return item in array


if __name__ == '__main__': # pragma: no coverage
    array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    print("L'array è:", array)
    item = int(input("Inserire elemento: "))

    if item:
        print("L'elemento è dentro l'array.")
    else:
        print("L'elemento non è dentro l'array")