""" 
Write a software that verifies if a number is present in a pre-defined array.

Output example:
Insert number 3
The number 3 is [not] present in the array.
"""

numbers = [1, 2, 3, 12, 89, 69, 133, 56, 99, 100000]


def look_for_number(number, array):
    if number in array:
        return True
    else:
        return False


wantedInt = int(input("Scegli un numero da cercare nell'array: "))

if look_for_number(wantedInt, numbers):
    print(f"{wantedInt} is in the array")
else:
    print(f"{wantedInt} is not in the array")
