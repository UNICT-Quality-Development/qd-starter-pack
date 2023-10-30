# Write a software that verifies if a number is present in a pre-defined array.

# Output example:
# Insert number 3
# The number 3 is [not] present in the array.

def isPresent(N: list, n: int) -> bool:
    return n in N

def main():
    n = int(input("Insert number: "))
    N = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
    if isPresent(N, n):
        print(f"The number {n} is present in the array.")
    else:
        print(f"The number {n} is not present in the array.")

if __name__ == "__main__":
    main()
