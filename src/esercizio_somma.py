#Write a program that takes as input two numbers and print the sum.
# Output:
# Insert the first number: 1
# Insert the second number: 2
#  Sum: 3

def main():
    a = int(input("Insert the first number: "))
    b = int(input("Insert the second number: "))
    print("Sum:", sum(a, b))

def sum(a: int, b: int) -> int:
    return a + b

if __name__ == "__main__":
    main()
