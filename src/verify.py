if __name__ == "__main__":
    
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)

    number = int(input("Insert number: "))

    if number in N: print(f"The number {number} is present in the array")
    else: print(f"The number {number} is not present in the array")
