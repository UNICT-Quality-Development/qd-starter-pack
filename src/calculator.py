#
#   Write a program that given two numbers as input make the main operations.
#
#   Output:
#   Insert first number: 4
#   Insert second number: 2
#
#   SUM: 6
#   Difference: 2
#   Multiplication: 8
#   Division: 2
#

def sum(a,b):
    return a+b

def difference(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        print("Impossibile eseguire la divisione\n")
        return
    return a/b


a_= int(input("Inserisci il primo numero\n"))
b_= int(input("Inserisci il secondo numero\n"))

print("Somma-> ", sum(a_,b_),"\n")
print("Sottrazione-> ", difference(a_,b_),"\n")
print("Moltiplicazione-> ", multiplication(a_,b_),"\n")
print("Divisione-> ", division(a_,b_),"\n")