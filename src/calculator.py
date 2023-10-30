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


val_1 = int(input('insert first number: '))
val_2=  int(input ('insert second number: '))

sum=val_1+val_2
dif=val_1-val_2
mul=val_1*val_2
div=float(val_1/val_2)

print('\nSum: ', SUM,'\nDifference: ', dif)
print('\nMultiplication', mul,'\nDivision', div)
