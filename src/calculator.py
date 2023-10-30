def sum(first, second):
    return first + second

def difference(first, second):
    return first - second

def multiplication(first, second):
    return first*second

def division(first, second):
    return first / second

x = int(input("Insert first number: "))
y = int(input("Insert second number: "))
print("SUM:" , sum(x, y))
print("Difference:" , difference(x, y))
print("Multiplication:" , multiplication(x, y))
print("Division:" , division(x, y))
