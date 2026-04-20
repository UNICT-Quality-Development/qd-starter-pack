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


def verify():
    try:
        number = int(input("Insert a number to test if it's present in the secret array: "))
    except:
        print("Invalid input!")
        return
    
    arr=[1,4,6,8,3,8,11,12,-4]
    for i in arr:
        if number == i:
            print("The number is in the array")
            return
    print("The number is NOT in the array")

verify()