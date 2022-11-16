# Write a software that verifies if a number is present in a pre-defined array.
# Output example:
# Insert number 3
# The number 3 is [not] present in the array.

def verify(value_list: list[int], value: int ):
  return int( value ) in value_list

if __name__ == '__main__':
  value_list = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
  value = 3
  if verify(value_list, value):
    print(f"The number {value} is  present in the array.")
  else:
    print(f"The number {value} is not present in the array.")