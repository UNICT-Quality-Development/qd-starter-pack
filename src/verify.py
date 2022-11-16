def check(n: list, number: int) -> bool:
    if number in n:
        return True
    return False

def main(N: list, number: int) -> str:
    if check(N, number) is True: 
        return f"The number {number} is present in the array"
    return f"The number {number} is not present in the array"

if __name__ == "__main__":
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)
    number = int(input("Insert number: "))

    print(main())
