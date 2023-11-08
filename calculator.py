def sum(a: int, b: int) -> int:
    return a + b

def diff(a: int, b: int)-> int:
    return a-b

def mul(a: int, b: int)-> int:
    return a*b

def div(a: int, b:int)-> int:
    return a/b

a= int(input ("Enter the first number: "))
b= int(input ("Enter the second number: "))

s= sum(a,b)
df= diff(a,b)
m= mul(a,b)
dv= div(a,b)

print (f"The sum is {s} ")
print (f"The difference is {df} ")
print (f"The multiplication is {m} ")
print (f"The division is {dv} ")