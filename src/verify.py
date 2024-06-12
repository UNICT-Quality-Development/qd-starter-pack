def isPresent(arr, dim, num):
    for i in range(dim):
        if arr[i] == num:
            return True

    return False

N = [3, 4, 5, 1, 2, 3, 4, 6, 13, 0]
x = int(input("Insert number "))
if isPresent(N, len(N), x):
    print(x, "is present in the array.")
else:
    print(x, "is not present in the array.")
