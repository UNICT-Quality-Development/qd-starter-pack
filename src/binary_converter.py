#
#   Write a program that given a number as input convert it in binary.
#
#   Output:
#   Insert first number: 8
#   The binary number is: 1000
#
def read_number()-> int:
  number = None
  while number is None:
    try:
      number = int(input("Insert first number: "))
    except ValueError as err:
      continue
  return number

def to_binary(number: int) -> str: 
  return "{0:b}".format(number)

if __name__ == '__main__':
  number = read_number()
  print(to_binary(number))