def verify(x :int) -> int:
    y = (2,3,5,6,7,12,15)
    if x in y:
        print("OK (Y)")
x = int(input())
verify(x)