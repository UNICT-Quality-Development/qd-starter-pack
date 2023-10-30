'''
Write a program that given two numbers as input make the main operations.

Output:
Insert first number: 4
Insert second number: 2

SUM: 6
Difference: 2
Multiplication: 8
Division: 2
'''
def calculator(first_number:int, second_number:int):
    sum = first_number + second_number
    difference = first_number - second_number
    multiplication = first_number * second_number
    if second_number != 0:
        division = first_number / second_number
    else:
        division = "Can't divide by 0"
    print(f"Sum: {sum}")
    print(f"Difference: {difference}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

first:int = int(input("Insert first number: "))
second:int = int(input("Insert second number: "))
calculator(first, second)
