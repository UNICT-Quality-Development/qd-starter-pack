#
# Write a software that verifies if a number is present in a pre-defined array.
#
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.
#
#

def verify(n, A):
    if n in A:
        print(f"The number {n} is present in the array.")
    else:
        print(f"The number {n} is not present in the array.")

array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

number = int(input("Insert number "))

verify(number, array)
