"""
  Write a program that given a number as input convert it in binary.

  Output:
  Insert first number: 8
  The binary number is: 1000
"""
print("Insert first number:")
inp_num = input()
binary_num = bin(int(inp_num))
print("Output:",binary_num[2:])
