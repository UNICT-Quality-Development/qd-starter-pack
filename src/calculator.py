def sum(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def divide(a, b):
    if (b == 0):
        print("Impossibile dividere per 0")
    else:
        return a / b
            
a = int(input("Inserisci il primo numero: "))
b = int(input("Inserisci il secondo numero: "))

print(sum(a,b))
print(subtraction(a, b))
print(multiplication(a, b))
print(divide(a,b))