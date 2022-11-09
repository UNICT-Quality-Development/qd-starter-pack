"""
  Write a program that given a number as input convert it in binary.
  Output:
  Insert first number: 8
  The binary number is: 1000
"""

def to_binary(n: int) -> int:
    return int(bin(n)[2:])
