
  # Write a program that given two numbers as input make the main operations.
  # Output:
  # Insert first number: 4
  # Insert second number: 2
  # SUM: 6
  # Difference: 2
  # Multiplication: 8
  # Division: 2

def calculator(num1: int, num2: int) -> int:
  print(f"SUM: {num1 + num2}")
  print(f"Difference: {num1 - num2}" )
  print(f"Multiplication: {num1 * num2}" )
  print(f"Division: {num1 / num2}" )


if __name__ == '__main__':
  num1 = input("Insert first number: ")
  num2 = input("Insert second number: ")

  calculator(int(num1),int(num2))