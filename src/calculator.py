import sys
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
def calculator(first:int, second:int)-> str:
    sum = first + second
    difference = first - second
    multiplication = first * second
    
    if second != 0:
        division = first / second
    else:
        division = "Can't divide by 0"
    
    print(f"Sum: {sum}")
    print(f"Difference: {difference}")
    print(f"Multiplication: {multiplication}")
    print(f"Division: {division}")

if(len(sys.argv) == 3):
    calculator(int(sys.argv[1]), int(sys.argv[2]))
else:
    print("Error! Use 2 args <first number> <second number>")