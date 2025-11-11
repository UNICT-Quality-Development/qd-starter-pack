#
# Write a software that verifies if a number is present in a pre-defined array.
#
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.
#
#
pre_defined_array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

if __name__ == "__main__":
    user_input = int(input("Insert number: "))

    if user_input in pre_defined_array:
        print("The element " + str(user_input) + " is present in the array")
    else:
        print("The element " + str(user_input) + " is not present in the array")
