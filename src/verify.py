'''
Write a software that verifies if a number is present in a pre-defined array.
Output example:
Insert number 3
The number 3 is [not] present in the array.
'''

def verify() -> None:
    N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    num = int(input("Insert number "))
    print(f'The number {num} is {"not" if num not in N else ""} present in the array')

if __name__ == "__main__":
    verify()
