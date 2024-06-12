"""
Write a program that takes as input two numbers and print the sum.
  Output:
  Insert the first number: 1
  Insert the second number: 2
  Sum: 3
"""
def sum(var_a: int, var_b: int)-> int:
    return var_a + var_b

x=int(input("Insert the first number: "))
y=int(input("Insert the second number: "))
print("Sum: ",sum(x,y))
