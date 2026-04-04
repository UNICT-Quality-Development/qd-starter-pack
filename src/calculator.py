x = input("Enter a number ")
y = input("Enter another number ")

x = float(x)
y = float(y)

def sum():
    print(f"Sum is {x + y}")
sum()

def diff():
    print(f"Difference is {x - y}")
diff()

def mult():
    print(f"Multiplication is {x * y}")
mult()

def div():
    if y != 0 :
        print(f"Division is {x / y}")
    else :
        print("Cannot divide by 0")
div()
