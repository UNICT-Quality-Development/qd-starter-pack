#Programm that checks if a value is present in a pre-defined array
def check(array: list, x) -> bool:
    for y in range(len(array)):
        if int(x) == array[y]:
            return True
    return False

array = list(range(1, 10, 2)) #[1 3 5 7 9]
x = input("What value (1-10) do you want to verify? ")
print(x,"is present in the array.") if (check(array, x)) else print(x,"is not present in the array.")