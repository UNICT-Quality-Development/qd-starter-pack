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

def calc(num1: int, num2: int) -> tuple:
    sum_result = num1 + num2
    difference_result = num1 - num2
    multiplication_result = num1 * num2
    division_result = num1 / num2 if num2 != 0 else "Undefined (division by zero)"
    
    return sum_result, difference_result, multiplication_result, division_result

if __name__ == "__main__":  # pragma: no cover
    
    sum_result, difference_result, multiplication_result, division_result = calc(2, 4)
    
    print(f"SUM: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Multiplication: {multiplication_result}")
    print(f"Division: {division_result}")