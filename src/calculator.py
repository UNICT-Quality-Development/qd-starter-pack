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

def sum(num1: int, num2: int) -> int:
    return num1 + num2

def diff(num1: int, num2: int) -> int:
    return num1 - num2

def mul(num1: int, num2: int) -> int:
    return num1 * num2

def div(num1: int, num2: int) -> float:
    if num2 == 0:
        return None  # Handle division by zero case
    return num1 / num2

def calc(num1: int, num2: int) -> tuple:
    sum_result = sum(num1, num2)
    difference_result = diff(num1, num2)
    multiplication_result = mul(num1, num2)
    division_result = div(num1, num2) 
    
    return sum_result, difference_result, multiplication_result, division_result


def main() -> None: # pragma: no cover
    num1 = int(input("Insert first number: "))
    num2 = int(input("Insert second number: "))
    
    sum_result, difference_result, multiplication_result, division_result = calc(num1, num2)
    
    print(f"SUM: {sum_result}")
    print(f"Difference: {difference_result}")
    print(f"Multiplication: {multiplication_result}")
    if division_result is None:
        print("Division: Undefined (division by zero)")
    else:
        print(f"Division: {division_result}")


if __name__ == "__main__":  # pragma: no cover
    main()

