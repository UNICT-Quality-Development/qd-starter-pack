# Write a software that verifies if a number is present in a pre-defined array.

# Output example:
# Insert number 3
# The number 3 is [not] present in the array.


Predefined_Array = [1, 5, 8, 12, 23, 30, 58, 72, 88]

Num_To_Check = int(input("Insert number: "))

if Num_To_Check in Predefined_Array:
    print("The number", Num_To_Check, "is present in the array")
else:
    print("The number", Num_To_Check, "is not present in the array")
