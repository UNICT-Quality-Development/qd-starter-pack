"""
Write a program that given a number as input convert it in binary.
Output:
Insert first number: 8
The binary number is: 1000
"""
def binary_convert(n:int)->int:
    return bin(n)

def main():
    print("Binary Converter")
    input_data= input("Input n: ")
    while not input_data.isdigit():
        print("Please enter a valid number.")
        input_data=input("Input n:")
    input_data=int(input_data)
    output=binary_convert(input_data)
    print(output[2:])

main()