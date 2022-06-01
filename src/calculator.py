
# Write a program that given two numbers as input make the main operations.
# Output:
# Insert first number: 4
# Insert second number: 2
# SUM: 6
# Difference: 2
# Multiplication: 8
# Division: 2

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b    

print("Insert first number:")
first_number = float ( input() )

print("Insert second number:")
second_number = float ( input() )

print( "sum:" , sum(first_number, second_number) )
print( "difference:" , difference(first_number, second_number) )
print( "multiplication:" , multiplication(first_number, second_number) )
print( "division:" , division(first_number, second_number) )