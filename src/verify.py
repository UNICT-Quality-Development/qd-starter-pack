"""
Write a software that verifies if a number is present in a pre-defined array.

Output example:
Insert number 3
The number 3 is [not] present in the array.
"""
array = [4,6,8,2,9]
print("Insert number:")
input_int = int(input())

def verify(input_int):
   if input_int in array:
       print("The number",input_int,"is present in the array")
   else: print("The number",input_int,"is not present in the array")
verify(input_int)
