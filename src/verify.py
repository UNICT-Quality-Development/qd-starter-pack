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


N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

num = int(input("Insert number: "))

if num in N:
    print(f"The number {num} is present in the array.")
else:
    print(f"The number {num} is not present in the array.")
