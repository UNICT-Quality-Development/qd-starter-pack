
arr = [3, 4, 5, 1, 2, 3, 4, 9, 13, 0]
print("Introdurre un numero")
x = input()

def verify(y):
    for i in arr:
        if y == i:
            return(True)
    return(False)

founded = verify(x)
print(founded)