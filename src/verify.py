def n_in_array(n: int, array: list[int]) -> bool:
    return n in array

def insert_integer() -> int:
    while True:
        print("insert a number")
        n_string = input().strip()
        if not n_string:
            print("That's not an int!")
        elif n_string.isdigit() or n_string.startswith('-') and n_string[1:].isdigit():
            return int(n_string)
        else:
            print("That's not an int!")

pre_def_array = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]

num = insert_integer()
not_string = " not" if not n_in_array(num, pre_def_array) else ""
print(f"The number {str(num)} is{not_string} present in the array.")
