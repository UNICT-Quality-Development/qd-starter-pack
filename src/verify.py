"""
Write a software that verifies if a number is present in a pre-defined array.

Output example:
Insert number 3
The number 3 is [not] present in the array.
"""

number=""
lista=[3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
while number.isdecimal() is False:
    number=input("Insert number: ")

if int(number) in lista:
    print("The number ",number," is present in the array.")
else:
    print("The number ",number," is not present in the array.")
