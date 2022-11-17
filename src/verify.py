def check(array: list, x: int) -> bool:
    return x in array

def main(vett: list, a: int) -> str:
    if check(vett, a) is True:
        return f"The number {a} is present in the array"
    return f"The number {a} is not present in the array"

if __name__ == "__main__":
    N = (3, 4, 5, 1, 2, 3, 4, 9, 13, 0)
    number = int(input("Insert number: "))

    print(main(N, number))
