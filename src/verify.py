#
# Write a software that verifies if a number is present in a pre-defined array.
#
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.
#
#

def verify(num, A):
    if num in A:
        print(f"The number {num} is present in the array.")
    else:
        print(f"The number {num} is not present in the array.")

N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

num = int(input("Insert number "))

verify(num, N)
