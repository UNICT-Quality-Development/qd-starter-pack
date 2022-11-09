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

def sum(a: int, b: int) -> int:
    return a + b

def sub(a: int, b: int) -> int:
    return a - b

def mul(a: int, b: int) -> int:
    return a * b

def div(a: int, b: int) -> int:
    return a / b if b != 0 else 0

def operations() -> None:
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))
    print()
    print(f'SUM: {sum(num1, num2)}')
    print(f'Difference: {sub(num1, num2)}')
    print(f'Multiplication: {mul(num1, num2)}')
    print(f'Division: {div(num1, num2)}')

if __name__ == "__main__":
    operations()
