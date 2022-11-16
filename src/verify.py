def verify(n: list, number: int) -> bool:
    if number in n:
        return True
    return False

def main():
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)

    number = int(input("Insert number: "))

    if verify(N, number) is True: 
        print(f"The number {number} is present in the array")
    else:
        print(f"The number {number} is not present in the array")

if __name__ == "__main__":
   main()
