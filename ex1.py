"""
  Write a program that given two numbers as input make the main operations.
  Output:
  Insert first number: 4
  Insert second number: 2
  SUM: 6
  Difference: 2
  Multiplication: 8
  Division: 2
"""

a = float(input("insert first value: "))
b = float(input("insert second value: "))

##-----------------------SUM---------------
def sum(a,b):
    return (a+b)
s = sum(a,b)
print(f"Sum:{s}")
##-----------------------DIFF--------------
def diff(a,b):
    return (a-b)
d = diff(a,b)
print(f"Difference:{d}")
##-----------------------DIV----------------
def div(a,b):
    return (a/b)
di = div(a,b)
print(f"Division:{di}")
##-----------------------MULT----------------
def mult(a,b):
    return (a*b)
m = div(a,b)
print(f"Division:{m}")