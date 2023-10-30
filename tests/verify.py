array = [1,2,3,4,5,6,7,8,9,0]

number = input("Enter a number to check if is present in the array:")

if int(number) in array:
    print(f"The number {number} is in the array")
else:
    print(f"The number {number} is not in the array")
