"""
  Write a program that given a number as input convert it in binary.

  Output:
  Insert first number: 8
  The binary number is: 1000
"""
print("Insert first number:")
input = int(input())
print("The binary number is:", bin(input).replace('0b', ''))